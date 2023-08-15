from rest_framework import serializers
from .models import Seasons # Count, CustomUser

# class CountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Count
#         fields = ('id', 'creation')


# class CustomUSerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'name', 'password')

class SeasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seasons
        fields = ('id', 'season_number', 'count', 'creation_date')