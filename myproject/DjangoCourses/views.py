from django.shortcuts import render,redirect
from Profile.models import *
# Create your views here.

#user auth mixin
class UserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and UserProfile.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect('/login/')
        return super().dispatch(request, *args, **kwargs)

def index(request):
    pass