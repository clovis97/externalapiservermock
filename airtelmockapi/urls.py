from django.urls import path
from .views import (
    AirtelB2CLoginMockView, AirtelC2BLoginMockView, AirtelC2BMockView,
    AirtelB2CMockView, AirtelDataMockView, AirtelTopupBalanceMockView,
    AirtelTopupMockView
)

urlpatterns = [
    path('airtel/b2c/login', AirtelB2CLoginMockView.as_view(), name='airtel-b2c-login'),
    path('airtel/c2b/login', AirtelC2BLoginMockView.as_view(), name='airtel-c2b-login'),
    path('airtel/c2b', AirtelC2BMockView.as_view(), name='airtel-c2b'),
    path('airtel/b2c', AirtelB2CMockView.as_view(), name='airtel-b2c'),
    path('airtel/data', AirtelDataMockView.as_view(), name='airtel-data'),
    path('airtel/topup/balance', AirtelTopupBalanceMockView.as_view(), name='airtel-topup-balance'),
    path('airtel/topup', AirtelTopupMockView.as_view(), name='airtel-topup'),
]
