from django.db import models
from django.db.models import Manager
# Create your models here.


class Buyer(models.Model):
    objects = Manager()
    name = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(decimal_places=2, default=0, max_digits=10)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):

    class Meta:
        verbose_name = "Список игр"
        ordering = ['-cost']

    objects = Manager()
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games', blank=True)

    def __str__(self):
        return self.title



