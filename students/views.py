from django.shortcuts import HttpResponse

# Create your views here.


def students(request):
    students = [
        {
            'id': 1,
            'name': 'John',
            'age': 20
        }
    ]
    from django.http import JsonResponse
    return JsonResponse({'students': students})