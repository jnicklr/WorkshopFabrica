from django.contrib import admin
from .models import Task

# Register your models here.

# admin.site.register(Task)

@admin.register(Task)
class UserAdmin(admin.ModelAdmin):
    model = Task
    fields = ['name', 'description', 'date', 'user']
