from django.shortcuts import render
from .models import Project
def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/list.html", {"projects": projects, "featured": [p for p in projects if p.featured], "others": [p for p in projects if not p.featured]})
