from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    headline = models.CharField(max_length=200)
    intro = models.TextField()
    bio = models.TextField()
    photo = models.ImageField(upload_to="profile/", blank=True)
    about_photo = models.ImageField(upload_to="profile/", blank=True)
    resume = models.FileField(upload_to="resume/", blank=True)
    location = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    available_for_hire = models.BooleanField(default=True)
    def __str__(self): return self.name
    @property
    def initials(self): return "".join(p[0] for p in self.name.split()[:2]).upper() or "P"
    @property
    def bio_paragraphs(self): return [p.strip() for p in self.bio.split("\n\n") if p.strip()]

class Achievement(models.Model):
    title = models.CharField(max_length=120)
    value = models.PositiveIntegerField()
    suffix = models.CharField(max_length=5, blank=True)
    description = models.CharField(max_length=200, blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    class Meta: ordering = ["order", "id"]
    def __str__(self): return self.title

class Skill(models.Model):
    name = models.CharField(max_length=80)
    CATEGORIES = [("backend", "Backend"), ("ai", "AI and data"), ("cloud", "Cloud and DevOps"), ("frontend", "Frontend"), ("tools", "Tools")]
    category = models.CharField(max_length=20, choices=CATEGORIES, default="backend")
    level = models.PositiveSmallIntegerField(default=80, validators=[MinValueValidator(1), MaxValueValidator(100)])
    order = models.PositiveSmallIntegerField(default=0)
    class Meta: ordering = ["order", "name"]
    def __str__(self): return self.name

class Experience(models.Model):
    role = models.CharField(max_length=140)
    company = models.CharField(max_length=140)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    summary = models.TextField(blank=True)
    highlights = models.TextField(blank=True)
    class Meta: ordering = ["-start_date"]
    def __str__(self): return f"{self.role} — {self.company}"
    @property
    def period(self): return f"{self.start_date.strftime('%b %Y')} to {self.end_date.strftime('%b %Y') if self.end_date else 'Present'}"
    @property
    def highlight_list(self): return [h.strip() for h in self.highlights.splitlines() if h.strip()]

class Education(models.Model):
    institution = models.CharField(max_length=160)
    degree = models.CharField(max_length=150)
    start_year = models.PositiveSmallIntegerField()
    end_year = models.PositiveSmallIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    class Meta: ordering = ["-start_year"]
    def __str__(self): return self.institution
    @property
    def period(self): return f"{self.start_year} to {self.end_year or 'Present'}"
