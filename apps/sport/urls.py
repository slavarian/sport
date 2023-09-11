from django.urls import path

# Local
from .views import index
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index),
    path('stavka/', views.create_bet, name='stavka'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', auth_views.LogoutView.as_view(), name='logout'),
    path('recharge_balance/', views.recharge_balance, name='recharge_balance'),
]
