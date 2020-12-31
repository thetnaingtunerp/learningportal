from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
# from ecoapp.models import *
from .forms import *
from .models import *
# Create your views here.
def profile(request):
    teams = TeamProfile.objects.all()
    context = {
        'teams':teams
    }
    return render(request, 'Profile/index.html', context)


def user_logout(request):
    logout(request)
    return redirect('profile')



def user_register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password1)
            login(request,user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "userprofile/userimage.png"
            data.save()
            # messages.success(request, '--- Success!---')
            return redirect('profile')
        else:
            messages.info(request,'--- Please try Again!---')
    else:
        form = SignupForm()

    context = {

        'form':form
    }
    return render(request, 'Profile/user_register.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
        # Return an 'invalid login' error message.
            messages.info(request, '--- Invalid Login, Please try Again!')

    context = {

    }
    return render(request, 'Profile/user_login.html', context)

