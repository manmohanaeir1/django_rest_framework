#from django.shortcuts import render
from django.http import JsonResponse
from .serializers import StudentSerializer 
from students.models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Mannual Serialization
"""
def studentsView(request):
    students = Student.objects.all()
    students_list = list(students.values())    # convert QuerySet to list of dictionaries called serialization  = > Mannual Serialization
    return JsonResponse( students_list, safe=False) # safe=False is required to serialize objects other than dict"
    
    """

    
# Automatic Serialization
@api_view(['GET'])
def studentsView(request):
     if request.method == 'GET':
            # get all students from the database
         students = Student.objects.all()
         serializer = StudentSerializer(students, many=True) # many=True is used when we want to serialize multiple objects
         return Response(serializer.data, status=status.HTTP_200_OK)
     