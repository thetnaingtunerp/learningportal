from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from Profile.models import *




#user auth mixin
class UserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and UserProfile.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect('/login/')
        return super().dispatch(request, *args, **kwargs)



class HtmlCourseView(UserRequiredMixin,TemplateView):
    template_name = 'Courses/htmlcourse.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_list'] = HTML_Course.objects.all().order_by('id')
        return context


class CourseDetailView(UserRequiredMixin,TemplateView):
    template_name = 'Courses/coursedetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_id = self.kwargs['id']
        courses = HTML_Course.objects.get(id=url_id)
        context['course'] = courses
        return context


#Bootstrap
class BootstrapCourseView(UserRequiredMixin,TemplateView):
    template_name = 'Courses/bootstrap_course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_list'] = BootstrapCourse.objects.all().order_by('id')
        return context


class BootstrapCourseDetailView(UserRequiredMixin,TemplateView):
    template_name = 'Courses/bootstrap_course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_id = self.kwargs['id']
        courses = BootstrapCourse.objects.get(id=url_id)
        context['course'] = courses
        return context

#CSS
class CssCourseView(UserRequiredMixin,TemplateView):
    template_name = 'Courses/css_course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_list'] = CssCourse.objects.all().order_by('id')
        return context


class CssCourseDetailView(UserRequiredMixin,TemplateView):
    template_name = 'Courses/css_course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_id = self.kwargs['id']
        courses = CssCourse.objects.get(id=url_id)
        context['course'] = courses
        return context

