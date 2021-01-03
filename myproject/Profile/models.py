from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# Create your models here.
class SettingProfile(models.Model):
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.TextField()
    website = models.CharField(max_length=200)

class UserProfile(models.Model):
    status = (('active','active'),('deactive','deactive'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='userprofile/')
    status = models.CharField(choices=status, default='deactive', max_length=225)

    def __str__(self):
        return self.user.username

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))
    image_tag.short_description = 'Image'

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

class TeamProfile(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    email = models.EmailField()
    facebook= models.CharField(max_length=200, blank=True)
    instagrm = models.CharField(max_length=200, blank=True)
    twetter = models.CharField(max_length=200, blank=True)
    gplus = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='userprofile/')

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))
    image_tag.short_description = 'Image'

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""


class MemberProfile(models.Model):
    status = (('active','active'),('deactive','deactive'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='userprofile/')
    status = models.CharField(choices=status, default='deactive', max_length=225)

    def __str__(self):
        return self.user.username

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))
    image_tag.short_description = 'Image'

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""
