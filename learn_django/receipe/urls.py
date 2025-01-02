from receipe import views
from django.urls import path

urlpatterns = [
    path('', views.receipe, name='receipe'), 
    path('login/', views.login, name='receipe'),   
    path('register/', views.register, name='receipe'),                         
    path('delete/<int:id>/', views.delete, name='receipe'),
    path('update/<int:id>/', views.update_receipe, name='receipe')
]
