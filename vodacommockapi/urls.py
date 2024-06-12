from django.urls import path
from .views import VodacashB2CMockView, VodacashB2CLoginMockView, VodacashC2BMockView, VodacashC2BLoginMockView, VodacashAirtimeBalanceMockView, VodacashAirtimeMockView

urlpatterns = [
    path('api/vodacash/b2c/mock', VodacashB2CMockView.as_view(), name='vodacash-b2c-mock'),
    path('api/vodacash/b2c/login/mock', VodacashB2CLoginMockView.as_view(), name='vodacash-b2c-login-mock'),
    path('api/vodacash/c2b/mock', VodacashC2BMockView.as_view(), name='vodacash-c2b-mock'),
    path('api/vodacash/c2b/login/mock', VodacashC2BLoginMockView.as_view(), name='vodacash-c2b-login-mock'),
    path('api/vodacash/airtime/balance/mock', VodacashAirtimeBalanceMockView.as_view(), name='vodacash-airtime-balance-mock'),
    path('api/vodacash/airtime/mock', VodacashAirtimeMockView.as_view(), name='vodacash-airtime-mock'),
]