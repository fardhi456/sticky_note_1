from django.contrib import admin 
from .models import TodoTask

@admin.register(TodoTask)
class TodoTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'index', 'title', 'due_date', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'due_date')
    search_fields = ('title', 'describtion')
    ordering = ('index', 'due_date')
    list_editable = ('is_completed',)

    fieldsets = (
        ('Task Info', {
            'fields': ('index', 'title', 'describtion', 'user')
        }),
        ('Dates & Status', {
            'fields': ('due_date', 'is_completed')
        }),
    )
