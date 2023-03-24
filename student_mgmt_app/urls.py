import django


from django.urls import path
from student_mgmt_app import views

urlpatterns=[
    path('',views.load_page,name='load_page'),
    path('login_page',views.login_page,name='login_page'),
    path('login',views.login,name='login'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('course_page',views.course_page,name='course_page'),
    path('add_course',views.add_course,name='add_course'),
    path('signup_page',views.signup_page,name='signup_page'),
    path('signup',views.signup,name='signup'),
    path('user_home',views.user_home,name='user_home'),
    path('teacher_details',views.teacher_details,name='teacher_details'),
    path('student_page',views.student_page,name='student_page'),
    path('add_student',views.add_student,name='add_student'),
    path('student_details',views.student_details,name='student_details'),
    path('teacher_page',views.teacher_page,name='teacher_page'),
    path('edit_userpage',views.edit_userpage,name='edit_userpage'),
    path('edit_profile/<int:pk>',views.edit_profile,name='edit_profile'),
    path('logout',views.logout,name='logout'),
    path('delete_teacher/<int:pk>',views.delete_teacher,name='delete_teacher'),
    path('delete_student/<int:pk>',views.delete_student,name='delete_student'),
]