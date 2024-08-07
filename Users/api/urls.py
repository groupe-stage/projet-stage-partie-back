from django.urls import path
from . import views

urlpatterns = [
    path('addUser/', views.addUser, name='add_user'),
    path('displayall/', views.displayall),
    path('updateusers/<int:id_user>/', views.updateUsers,name='updateUsers'),
    path('deleteusers/<int:id_user>/', views.deleteUsers, name='deleteUsers'),
]
