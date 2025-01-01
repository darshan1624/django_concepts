from receipe import views
from django.urls import path

urlpatterns = [
    path('', views.receipe, name='receipe')    
]
