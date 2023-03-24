from django.contrib import admin
from student_mgmt_app.models import course_model,teacher_model

# Register your models here.

@admin.register(course_model)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','course_name','course_fee')

@admin.register(teacher_model)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','teacher','course','address','age','image')
