from django.urls import path
from .views import *

app_name = 'courses'
urlpatterns = [
    path('', HtmlCourseView.as_view(), name='htmlcourse'),
    path('coursedetail/<int:id>/', CourseDetailView.as_view(), name='coursedetail'),
    path('bootstrap/', BootstrapCourseView.as_view(), name='bootstrapcourse'),
    path('bootstrapdetail/<int:id>/', BootstrapCourseDetailView.as_view(), name='bootstrapdetail'),
]