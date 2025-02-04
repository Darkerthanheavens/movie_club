from django.contrib import admin
from .models import Movies, Comment
# Register your models here.

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    pass