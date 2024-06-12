from django.urls import path
from .views import *

urlpatterns = [
    path('ussd/', USSDView.as_view(), name='ussd-view'),
    ]