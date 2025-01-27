from receipe import views
from django.urls import path

urlpatterns = [
    path('', views.receipe, name='receipe'),                        
    path('delete/<int:id>/', views.delete, name='receipe'),
    path('update/<int:id>/', views.update_receipe, name='receipe'),
    path('students', views.get_students, name='students'),
    path('see_marks/<student_id>/', views.see_marks, name='see_marks'),

]
