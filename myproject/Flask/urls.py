from django.urls import path
from .views import *

app_name = 'flask'
urlpatterns = [
    path('flask_courses/', FlaskCourseView.as_view(), name='flaskcourse'),
    path('flask_course_detail/<int:id>/', FlaskCourseDetailView.as_view(), name='flaskdetail'),

]