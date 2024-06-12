from django.urls import path
from .views import (
    OrangeB2CMockView, OrangeC2BMockView, OrangeAiritmeBalanceMockView,
    OrangeAirtimeMockView, OrangeAirtimeCheckTransMockView, OrangeSmsMockView,
    OrangeCashBalanceMockView, OrangeCashCheckTransMockView
)

urlpatterns = [
    path('orange/b2c', OrangeB2CMockView.as_view(), name='orange-b2c-mock'),
    path('orange/c2b', OrangeC2BMockView.as_view(), name='orange-c2b-mock'),
    path('orange/airtime/balance', OrangeAiritmeBalanceMockView.as_view(), name='orange-airtime-balance-mock'),
    path('orange/airtime', OrangeAirtimeMockView.as_view(), name='orange-airtime-mock'),
    path('orange/airtime/check-trans', OrangeAirtimeCheckTransMockView.as_view(), name='orange-airtime-check-trans-mock'),
    path('orange/sms', OrangeSmsMockView.as_view(), name='orange-sms-mock'),
    path('orange/cash/balance', OrangeCashBalanceMockView.as_view(), name='orange-cash-balance-mock'),
    path('orange/cash/check-trans', OrangeCashCheckTransMockView.as_view(), name='orange-cash-check-trans-mock'),
]
