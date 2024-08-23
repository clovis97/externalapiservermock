from django.urls import path
from .views import (
    AfricellB2CMockView, AfricellBalanceCheckMockView, AfricellDataBundleMockView,
    AfricellDataBundleListMockView, AfricellSendSmsMockView, AfricellTopUpMockView,
    AfricellTransactionLoadMockView
)

urlpatterns = [
    path('africell/b2c', AfricellB2CMockView.as_view(), name='africell-b2c'),
    path('africell/GetBalance', AfricellBalanceCheckMockView.as_view(), name='africell-balance-check'),
    path('africell/RechargeBundles', AfricellDataBundleMockView.as_view(), name='africell-data-bundle'),
    path('africell/data/bundle/list', AfricellDataBundleListMockView.as_view(), name='africell-data-bundle-list'),
    path('africell/send/sms', AfricellSendSmsMockView.as_view(), name='africell-send-sms'),
    path('africell/SubscriberCreditTransfer', AfricellTopUpMockView.as_view(), name='africell-topup'),
    path('africell/transaction/load', AfricellTransactionLoadMockView.as_view(), name='africell-transaction-load'),
]
