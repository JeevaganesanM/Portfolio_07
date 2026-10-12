from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=120)
    summary = models.TextField()
    impact = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="projects/", blank=True)
    tech = models.CharField(max_length=250)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)
    class Meta: ordering = ["order", "-year", "id"]
    def __str__(self): return self.title
    @property
    def tech_list(self): return [t.strip() for t in self.tech.split(",") if t.strip()]
    @property
    def tags(self): return self.tech_list
    @property
    def source_url(self): return self.github_url
