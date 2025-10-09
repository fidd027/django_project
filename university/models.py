
from django.db import models





class Teachers(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()

    class Meta:
        db_table = 'teachers'

class Course(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    credit = models.IntegerField()

    class Meta:
        db_table = 'courses'


class Students(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    dob = models.DateField()
    course = models.ManyToManyField(Course)

    class Meta:
        db_table = 'students'

