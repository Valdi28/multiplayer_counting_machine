from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('seasons/', views.SeasonsView.as_view(), name="seasons"),
    path('season/', views.SeasonsView.as_view(), name="season"),
    path('season/<int:season_number>/', views.SeasonView.as_view(), name="specific_season"),
    path('season/<int:season_number>/count/', views.SeasonCountView.as_view(), name="season_count"),
    path('season/latest/', views.LatestSeasonView.as_view(), name="latest_season"),
    path('season/latest/count/', views.LatestSeasonCountView.as_view(), name="latest_season_count")
]

# :) 