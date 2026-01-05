from django.urls import path
from .views import *

urlpatterns = [
    path("content/", get_content, name="get_content"),
    path("course/<int:course_id>/", course_detail, name="course_detail"),
    path("courses/", course_list, name="course_list"),
    path("members/", members_list, name="members_list"),

]
