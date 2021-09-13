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