from django.urls import path
from .views import *

app_name = 'jquery'
urlpatterns = [
    path('jquery_course/', JqueryCourseView.as_view(), name='jquery_course'),
    path('jquery_course_detail/<int:id>/', JqueryCourseDetailView.as_view(), name='jquery_course_detail'),

]