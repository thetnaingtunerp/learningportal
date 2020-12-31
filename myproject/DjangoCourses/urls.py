from django.urls import path
from .views import *

app_name = 'django'
urlpatterns = [
    path('django_courses/', DjangoCourseView.as_view(), name='djangocourse'),
    path('django_course_detail/<int:id>/', DjangoCourseDetailView.as_view(), name='djangodetail'),

]