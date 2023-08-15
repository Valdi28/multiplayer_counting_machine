from django.urls import path
from  rest_framework_simplejwt import views as jwtViews
from . import views

urlpatterns = [
    path('token/', jwtViews.TokenObtainPairView.as_view(), name='auth_token_obtain'),
    path('token/refresh/', jwtViews.TokenRefreshView.as_view(), name='auth_token_refresh'),
    path('logout/', views.Logout.as_view())
]