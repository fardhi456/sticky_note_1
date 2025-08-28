# filters.py
import django_filters
from .models import TodoTask

class TodoTaskFilter(django_filters.FilterSet):

    class Meta:
        model = TodoTask
        fields = ['index', 'title', 'describtion', 'due_date', 'created_at', 'is_completed', ]
