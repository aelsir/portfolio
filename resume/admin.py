from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Role, Project, Work, Skill)
class RoleAdmin(admin.ModelAdmin):
    pass