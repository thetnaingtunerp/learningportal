from django.urls import path
from .views import *

app_name = 'javascript'
urlpatterns = [
    path('javascript_course/', JavascriptCourseView.as_view(), name='javascript_course'),
    path('javascript_course_detail/<int:id>/', JavascriptCourseDetailView.as_view(), name='javascript_course_detail'),

]