import django_filters
from .models import Student

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'student_name': ['icontains'],
            'remarks': ['exact'],
        }
