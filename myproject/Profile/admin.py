from django.contrib import admin
from .models import *
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone','address','city','image_tag','status']


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(SettingProfile)