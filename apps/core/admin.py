from django.contrib import admin
from .models import Achievement, Profile, Skill, Experience, Education
admin.site.register([Achievement, Skill, Experience, Education])
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "available_for_hire")
    def has_add_permission(self, request): return not Profile.objects.exists()
