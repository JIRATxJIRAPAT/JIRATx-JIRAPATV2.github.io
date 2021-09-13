from django.db import models

# Create your models here.

class Course(models.Model):
    course_code = models.CharField(max_length=5 , primary_key= True)
    course_name = models.CharField(max_length=64)
    semester = models.PositiveIntegerField()
    academic_year = models.PositiveIntegerField()
    limit = models.PositiveIntegerField()
    status = models.BooleanField()

    def __str__(self):
        return f"{self.course_code} {self.course_name}"
    
class Student(models.Model):
    student_name = models.CharField(max_length = 50)
    student_id = models.CharField(max_length = 10)
    grade = models.FloatField()
    years = models.PositiveIntegerField()
    enrollment = models.ManyToManyField(Course,blank = True,related_name="member")
    
    def __str__(self):
        return f"{self.student_id}: {self.student_name}"