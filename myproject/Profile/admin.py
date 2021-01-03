from django.contrib import admin
from .models import *
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone','address','city','image_tag','status']

class MemberProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone','address','city','image_tag','status']

class TeamProfileAdmin(admin.ModelAdmin):
    list_display = ['name','role','email']


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(MemberProfile,MemberProfileAdmin)
admin.site.register(SettingProfile)
admin.site.register(TeamProfile,TeamProfileAdmin)
