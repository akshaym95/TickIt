from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'due_date', 'completed', 'created_at')
    list_filter = ('completed', 'priority', 'created_at', 'due_date')
    search_fields = ('title', 'description', 'user__username')
    list_editable = ('completed', 'priority')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'description', 'user')
        }),
        ('Status & Priority', {
            'fields': ('completed', 'priority')
        }),
        ('Timing', {
            'fields': ('due_date', 'created_at', 'updated_at', 'completed_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at', 'completed_at')
