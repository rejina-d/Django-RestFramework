from django.contrib import admin
from .models import Project


class ProjectAdmin (admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')

# Register your models here.
admin.site.register(Project)
