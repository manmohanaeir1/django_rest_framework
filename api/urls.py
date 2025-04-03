from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView),  # function based view   
    path('students/<int:pk>/', views.studentDetailView),  # function based view
]
