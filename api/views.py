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
@api_view(['GET', 'POST']) # this decorator is used to specify the allowed methods for the view
def studentsView(request):
     if request.method == 'GET':
            # get all students from the database
         students = Student.objects.all()
         serializer = StudentSerializer(students, many=True) # many=True is used when we want to serialize multiple objects
         return Response(serializer.data, status=status.HTTP_200_OK)
     elif request.method == 'POST':
            serializer = StudentSerializer(data=request.data) # data=request.data is used to get the data from the request
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


@api_view(['GET'])

def studentDetailView(request,pk):     
# this view is used to get, update and delete a student by id
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)