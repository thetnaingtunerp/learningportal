from django.contrib import admin
from .models import *

# Register your models here.

class HTMLCoruse(admin.ModelAdmin):
    list_display = ['title','created_at','image_tag']
    list_filter = ['title']

class CssCoruseAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','image_tag']
    list_filter = ['title']

class BootstrapCoruseAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','image_tag']
    list_filter = ['title']

admin.site.register(HTML_Course,HTMLCoruse)
admin.site.register(CssCourse,CssCoruseAdmin)
admin.site.register(BootstrapCourse,BootstrapCoruseAdmin)