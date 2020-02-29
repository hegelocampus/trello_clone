from django.contrib import admin

from .models import Project, Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline]
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Project, ProjectAdmin)

