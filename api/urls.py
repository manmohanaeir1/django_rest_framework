from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeesViewSet, basename='employees')


urlpatterns = [
    path('students/', views.studentsView),  # function based view   
    path('students/<int:pk>/', views.studentDetailView),  # function based view



    # path('employees/', views.Employees.as_view()),  # class based view
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),  # class based view


    path('', include(router.urls) )  # class based view
]


