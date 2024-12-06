from django.contrib import admin
from .models import Game, Buyer


admin.site.register(Buyer)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'description', 'age_limited',)
    list_filter = ('buyer',)
    search_fields = ('title',)
    list_per_page = 15

    fieldsets = [
        ("Редактировать", {
             'fields': ('title', 'cost', 'description', 'size'),
         }, ),
        (None, {
            "fields": ["age_limited", ],
        }, ),
    ]

# Register your models here.
