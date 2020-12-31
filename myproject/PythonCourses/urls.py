from django.urls import path
from .views import *

app_name = 'pythonoop'
urlpatterns = [
    path('python_courses/', PythonCourseView.as_view(), name='python_courses'),
    path('python_course_detail/<int:id>/', PythonCourseDetailView.as_view(), name='python_course_detail'),
    path('tkinter_courses/', PythonCourseView.as_view(), name='tkinter_courses'),
    path('tkinter_course_detail/<int:id>/', PythonCourseDetailView.as_view(), name='tkinter_course_detail'),

]