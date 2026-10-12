import math
import markdown
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe

class ArticleQuerySet(models.QuerySet):
    def published(self): return self.filter(is_published=True, published_on__lte=timezone.localdate())

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=300)
    body = models.TextField()
    cover = models.ImageField(upload_to="articles/", blank=True)
    published_on = models.DateField(default=timezone.localdate)
    is_published = models.BooleanField(default=True)
    objects = ArticleQuerySet.as_manager()
    class Meta: ordering = ["-published_on", "-id"]
    def __str__(self): return self.title
    def get_absolute_url(self): return reverse("articles:detail", kwargs={"slug": self.slug})
    @property
    def body_html(self): return mark_safe(markdown.markdown(self.body, extensions=["fenced_code", "tables", "sane_lists"]))
    @property
    def reading_minutes(self): return max(1, math.ceil(len(self.body.split()) / 220))
    @property
    def excerpt(self): return self.summary
    @property
    def published_at(self): return self.published_on
