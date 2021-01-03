from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.views.generic import *
from Profile.models import *
from .models import *
# Create your views here.

#user auth mixin
class UserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and UserProfile.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect('/login/')
        return super().dispatch(request, *args, **kwargs)


class MemberRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and MemberProfile.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect('/login/')
        return super().dispatch(request, *args, **kwargs)


class FlaskCourseView(MemberRequiredMixin,TemplateView):
    template_name = 'Flask/flask_course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_list'] = FlaskCourse.objects.all().order_by('id')
        return context


class FlaskCourseDetailView(MemberRequiredMixin,TemplateView):
    template_name = 'Flask/flask_course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_id = self.kwargs['id']
        courses = FlaskCourse.objects.get(id=url_id)
        context['course'] = courses
        return context

