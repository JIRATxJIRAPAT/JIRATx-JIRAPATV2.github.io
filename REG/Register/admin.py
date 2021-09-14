from django.contrib import admin

# Register your models here.

from .models import Course
class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_code","course_name","status")

#class StudentUser(admin.ModelAdmin):
    #filter_horizontal = ("enrollment",)

admin.site.register(Course,CourseAdmin)
#admin.site.register(Student,StudentUser)