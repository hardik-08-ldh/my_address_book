from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('add_address',views.AddAddressView,name='add_address')
]
