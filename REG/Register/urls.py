from django.urls import path

from . import views

app_name ="Register"

urlpatterns = [
    path('',views.index,name='index'),
    path('<course_code>',views.ShowCourse,name='ShowCourse'),
    path("<course_code>/apply", views.apply, name="apply"),
    path("<course_code>/remove", views.removeCourse, name="remove"),
]