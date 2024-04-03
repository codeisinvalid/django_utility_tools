from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created', 'complete')
# Register your models here.
admin.site.register(Task, TaskAdmin)
