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


class PythonCourseView(UserRequiredMixin,TemplateView):
    template_name = 'pythoncourses/python_course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_list'] = PythonCourse.objects.all().order_by('id')
        return context


class PythonCourseDetailView(UserRequiredMixin,TemplateView):
    template_name = 'pythoncourses/python_course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_id = self.kwargs['id']
        courses = PythonCourse.objects.get(id=url_id)
        context['course'] = courses
        return context


class TkinterCourseView(UserRequiredMixin,TemplateView):
    template_name = 'pythoncourses/tkinter_course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_list'] = PythonCourse.objects.all().order_by('id')
        return context


class TkinterCourseDetailView(UserRequiredMixin,TemplateView):
    template_name = 'pythoncourses/tkinter_course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_id = self.kwargs['id']
        courses = PythonCourse.objects.get(id=url_id)
        context['course'] = courses
        return context

