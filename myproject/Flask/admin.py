from django.contrib import admin
from .models import *
# Register your models here.

class FlaskCoruseAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','image_tag']
    list_filter = ['title']

admin.site.register(FlaskCourse,FlaskCoruseAdmin)