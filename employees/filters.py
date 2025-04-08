import django_filters as filters
from .models import Employee    

class EmployeeFilter(filters.FilterSet):
     emp_designation = filters.CharFilter(field_name='emp_designation', lookup_expr='icontains')
     emp_name = filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
     #id = filters.RangeFilter(field_name='id')
     id_min =filters.CharFilter(method = 'filter_by_id_range', label= 'ID Min')
     id_max = filters.CharFilter(method = 'filter_by_id_range', label= 'ID Max') 


     class Meta:
            model = Employee
            fields = ['emp_designation', 'emp_name', 'id_min', 'id_max']   

     def filter_by_id_range(self, queryset, name, value):
            id_min = self.data.get('id_min')
            id_max = self.data.get('id_max')
            if id_min and id_max:
                return queryset.filter(emp_id__range=(id_min, id_max))
            return queryset
            