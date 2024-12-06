from rest_framework import serializers
from .models import Game


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['title', 'cost', 'size', 'description', 'age_limited']
