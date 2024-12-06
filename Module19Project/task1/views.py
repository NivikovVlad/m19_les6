from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RegistrationForm
from .models import Buyer, Game
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import GamesSerializer


# Create your views here.
def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in [user.name for user in users]:
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, age=age)
                return render(request, 'main.html')
    else:
        form = RegistrationForm()
    info['form'] = form
    return render(request, 'registration_page.html', info)


class PageMain(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(PageMain, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class Shop(TemplateView):
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        games = Game.objects.all().order_by('title')
        if games is None:
            games = ['', '']
        kol_product = self.request.GET.get('kol_product')
        if not kol_product:
            kol_product = 12
        page_number = self.request.GET.get('page')
        paginator = Paginator(games, kol_product)
        page_games = paginator.get_page(page_number)

        context = super(Shop, self).get_context_data(**kwargs)
        context['games'] = games
        context['title'] = 'Магазин'
        context['page_games'] = page_games
        context['kol_product'] = kol_product

        return context


class Basket(TemplateView):
    template_name = 'basket.html'

    def get_context_data(self, **kwargs):
        context = super(Basket, self).get_context_data(**kwargs)
        context['title'] = 'Корзина'
        return context



@api_view(['GET'])
def games_list_api(request):
    products = Game.objects.all()
    serializer = GamesSerializer(products, many=True)
    return Response(serializer.data)