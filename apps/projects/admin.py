from django.contrib import admin
from .models import Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "featured", "order")
    list_editable = ("featured", "order")
    search_fields = ("title", "tech")
