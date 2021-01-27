from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('add_address',views.AddAddressView,name='add_address'),
    path('edit_address/<list_id>',views.EditAddressView,name="edit_address"),
    path('delete/<list_id>',views.DeleteView,name="delete_address"),
]
