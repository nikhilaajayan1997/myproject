from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class course_model(models.Model):
    course_name=models.CharField(max_length=120)
    course_fee=models.IntegerField()

class teacher_model(models.Model):
    teacher=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(course_model,on_delete=models.CASCADE,null=True)
    address=models.TextField(max_length=250)
    age=models.IntegerField()
    image=models.ImageField(null=True,blank=True,upload_to='image/')

class student_model(models.Model):
    student=models.ForeignKey(course_model,on_delete=models.CASCADE,null=True)
    std_name=models.TextField(max_length=120)
    std_address=models.TextField(max_length=250)
    std_age=models.IntegerField()
    join_date=models.DateField(auto_now_add=True)
    std_image=models.ImageField(null=True,blank=True,upload_to='image/')
