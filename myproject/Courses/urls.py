from django.urls import path
from .views import *

app_name = 'courses'
urlpatterns = [
    path('', HtmlCourseView.as_view(), name='htmlcourse'),
    path('coursedetail/<int:id>/', CourseDetailView.as_view(), name='coursedetail'),
    path('bootstrap/', BootstrapCourseView.as_view(), name='bootstrapcourse'),
    path('bootstrapdetail/<int:id>/', BootstrapCourseDetailView.as_view(), name='bootstrapdetail'),
    path('css/', CssCourseView.as_view(), name='css_course'),
    path('css_course_detail/<int:id>/', CssCourseDetailView.as_view(), name='css_course_detail'),
]