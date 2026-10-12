from django.shortcuts import render
from .portfolio_data import ACHIEVEMENTS, EDUCATION, PROJECTS, SKILLS
def home(request): return render(request, "core/static_home.html", {"achievements": ACHIEVEMENTS, "projects": PROJECTS})
def about(request): return render(request, "core/static_about.html", {"education": EDUCATION, "skills": SKILLS})
def projects(request): return render(request, "core/static_projects.html", {"projects": PROJECTS})
def contact(request): return render(request, "core/static_contact.html")
