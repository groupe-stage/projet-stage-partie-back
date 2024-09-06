from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addSallex, name='add_sallex'),
    path('all/', views.displayall, name='display_all_sallex'),
    path('delete/<int:idse>/', views.deleteSallex, name='delete_sallex'),
]
