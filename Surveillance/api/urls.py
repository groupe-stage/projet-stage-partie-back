from django.urls import path
from . import views

urlpatterns = [
    path('add-surveillance/', views.addSurveillance, name='add-surveillance'),
    path('all-surveillances/', views.displayAllSurveillances, name='display-all-surveillances'),
    path('update-surveillance/<int:id>/', views.updateSurveillance, name='update-surveillance'),
    path('delete-surveillance/<int:id>/', views.deleteSurveillance, name='delete-surveillance'),
    path('surveillance/<int:id>/', views.getSurveillance, name='get-surveillance'),
]
