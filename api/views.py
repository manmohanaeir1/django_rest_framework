from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .serializers import StudentSerializer,EmployeeSerializer 
from students.models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins, generics,viewsets

from employees.filters import EmployeeFilter

# Mannual Serialization
"""
def studentsView(request):
    students = Student.objects.all()
    students_list = list(students.values())    # convert QuerySet to list of dictionaries called serialization  = > Mannual Serialization
    return JsonResponse( students_list, safe=False) # safe=False is required to serialize objects other than dict"
    
    """

    
# Automatic Serialization  
#function based view
# this view is used to get all students and create a new student
# this view is used to get, update and delete a student by id
 


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


@api_view(['GET','PUT', 'DELETE']) # this decorator is used to specify the allowed methods for the view

def studentDetailView(request,pk):     
# this view is used to get, update and delete a student by id
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
         serializer = StudentSerializer(student, data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

         else:
                print(serializer.errors)   
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



   # # class based view
   # 


# class Employees(APIView):
#      def get(self, request):
#           employees = Employee.objects.all()
#           serializer = EmployeeSerializer(employees, many=True)     
#           return Response(serializer.data, status=status.HTTP_200_OK)

#      def post(self, request):
#           serializer = EmployeeSerializer(data=request.data)
#           if serializer.is_valid():
#                serializer.save()
#                return Response(serializer.data, status=status.HTTP_201_CREATED)
#           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

# class EmployeeDetail(APIView):
#      def get_object(self, pk):
#           try:
#                employee = Employee.objects.get(pk=pk)
#                return employee
#           except Employee.DoesNotExist:
#                raise Http404    
          
#      def get(self, request, pk):
#           employee = self.get_object(pk)
#           serializer = EmployeeSerializer(employee)
#           return Response(serializer.data, status=status.HTTP_200_OK)
           

#      def put(self, request, pk):
#           employee = self.get_object(pk) # get the employee object by id
#           serializer = EmployeeSerializer(employee, data=request.data)      #
#           if serializer.is_valid():
#                  serializer.save()
#                  return Response(serializer.data, status=status.HTTP_200_OK)
#           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#      def delete(self, request, pk):
#           employee = self.get_object(pk) #  
#           employee.delete()
#           return Response(status=status.HTTP_204_NO_CONTENT)     


"""""
# Misings 

class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView): # class based view
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer


     def get(self, request):
        return self.list(request) # this method is used to get all employees from the database
    
     def post(self, request):
        return self.create(request) # this method is used to create a new employee in the database
 
#mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin
class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView): # class based view
      queryset = Employee.objects.all()
      serializer_class = EmployeeSerializer

      def get(self, request, pk):
            return self.retrieve(request, pk) # this method is used to get a employee by id 
       
      def put(self, request, pk):
           return self.update(request, pk) # prepopulate the data in the form and update the employee in the database
      
      def delete(self, request, pk):
           return self.destroy(request, pk)

"""            

"""
#Generic API View

class Employees(generics.ListCreateAPIView): #ListAPIView = accept the incomming reques and also send the response 
  
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer



class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView): # this view is used to get, update and delete a employee by id
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer
     lookup_field = 'pk' # this is used to specify the field to be used for lookup
     
"""


"""
#Viewset

class EmployeesViewSet(viewsets.ViewSet):
     def list(self, request):
          queryset = Employee.objects.all()
          serializer = EmployeeSerializer(queryset, many=True)
          return Response(serializer.data, status=status.HTTP_200_OK)
     

     def create(self, request):
        
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

     def retrieve(self,request, pk=None):
          employee = get_object_or_404(Employee, pk=pk)
          serializer = EmployeeSerializer(employee)
          return Response(serializer.data, status=status.HTTP_200_OK)
     

     def update(self, request, pk=None):
          employee = get_object_or_404(Employee, pk=pk)
          serializer = EmployeeSerializer(employee, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_200_OK)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
             

     def delete(self, request,pk=None):
          employee = get_object_or_404(Employee, pk=pk)
          employee.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)

"""

# model viewset => to reduce the code and make it more readable


class EmployeesViewSet(viewsets.ModelViewSet):   
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer
        #filterset_fields =['emp_designation'] # this is used to filter the employees by department 
        filterset_class = EmployeeFilter # this is used to filter the employees by department using django_filters 

        # by that code we can get all employees, 
        # create a new employee, get a employee by id,
        #  update a employee by id and delete a employee by id` Pk and NonPk 
 