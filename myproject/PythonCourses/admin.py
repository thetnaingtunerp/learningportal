from django.contrib import admin
from .models import *
# Register your models here.

class PythonCoruseAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','image_tag']
    list_filter = ['title']


class TkinterCourseAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','image_tag']

admin.site.register(PythonCourse,PythonCoruseAdmin)
admin.site.register(TkinterCourse,TkinterCourseAdmin)