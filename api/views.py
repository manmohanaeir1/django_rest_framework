from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def studentsView(request):
    students = [
        {
            'id': 1,
            'name': 'John',
            'age': 20
        },
        {
            'id': 2,
            'name': 'Jane',
            'age': 22
        },
        {
            'id': 3,
            'name': 'Doe',
            'age': 21
        }
    ]
    return JsonResponse({'students': students})