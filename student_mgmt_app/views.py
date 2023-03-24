from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from student_mgmt_app.models import *

# Create your views here.

def load_page(request):
    return render(request,'home.html')
    
def login_page(request):
    return render(request,'login.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                return redirect('admin_home')
            else:
                 auth.login(request,user)
                 return redirect('user_home')


def admin_home(request):
    return render(request,'admin_home.html')

def user_home(request):
    return render(request,'user_home.html')

def signup_page(request):
    courses=course_model.objects.all()
    context={'courses':courses}
    return render(request,'signup.html',context)

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        address=request.POST['address']
        age=request.POST['age']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        course=request.POST['select']
        image=request.FILES.get('file')

        if password==cpassword:
            if User.objects.filter(username=username).exists(): 
                messages.info(request,'this username already exists')
                return redirect('login_page')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'this email already exists')
                return redirect('login_page')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,
                                           email=email,username=username,password=password)
                user.save()
                print('successed.......')

                data=User.objects.get(id=user.id)
                cdata=course_model.objects.get(id=course)
                user_data=teacher_model(address=address,age=age,image=image,teacher=data,course=cdata)
                user_data.save()
                print('success:::::::::::')
                return redirect('login_page')
        else:
            messages.info(request,'password already exists')
            return redirect('login_page')



def course_page(request):
    return render(request,'course.html')

def add_course(request):
    if request.method=='POST':
        course_name=request.POST['course_name']
        course_fee=request.POST['course_fee']
        data=course_model(course_name=course_name,course_fee=course_fee)
        data.save()
        return redirect('admin_home')

def teacher_details(request):
    teacher_detail=teacher_model.objects.all()   
    return render(request,'teacher_detail.html',{'teachers':teacher_detail})

def student_page(request):
    course=course_model.objects.all()
    return render(request,'student.html',{'course':course})

def add_student(request):
    if request.method=='POST':
        course=request.POST['select']
        std_name=request.POST['std_name']
        std_address=request.POST['std_address']
        std_age=request.POST['std_age']
        std_image=request.FILES.get('file')

        cdata=course_model.objects.get(id=course)
        
        data=student_model(student=cdata,std_name=std_name,std_address=std_address,
                   std_age=std_age,std_image=std_image)
        data.save()
        return redirect('admin_home')

def student_details(request):
    student=student_model.objects.all()
    return render(request,'student_detail.html',{'student':student})

def teacher_page(request):
   users=teacher_model.objects.get(teacher=request.user)
   return render(request,'teacher_profile.html',{'user':users})

def edit_userpage(request):
    users=teacher_model.objects.get(teacher=request.user)
    cdata=course_model.objects.all()
    return render(request,'edit_profile.html',{'user':users,'cdata':cdata})

def edit_profile(request):
    if request.method=='POST':
        user=teacher_model.objects.get(teacher=request.user)
        # user1=User.objects.filter(id=request.user)
        # user1=User.objects.get(request.user)
        # student=student_table.objects.get(id=pk)
        # student.first_name=request.POST.get('first_name')
        # student.last_name=request.POST.get('last_name')
        # student.email=request.POST.get('email_id')
        # student.phone=request.POST.get('phone_no')
        # student.course=request.POST.get('course_name')
        # student.address=request.POST.get('address')
        # student.image=request.FILES.get('file')
        # old=student.image
        # new=request.FILES.get('file')
        # if old != NULL and new == NULL:
        #     student.image=old
        # else:
        #     student.image=new
        if len(request.FILES)!=0:
            # if len(student.image)>0:
            #     os.remove(student.image.path)
           user.image=request.FILES['file']
        
        course=request.POST.get('select')
        cdata=course_model.objects.get(id=course) 
        user.teacher.email=request.POST.get('email')
        user.age=request.POST.get('age')
        user.course=cdata
        user.address=request.POST.get('address')
        user.teacher.username=request.POST.get('username')
        user.teacher.first_name=request.POST.get('first_name')
        user.teacher.last_name=request.POST.get('last_name')
            # student.image=request.FILES.get('file')  
            # cdata=course_model.objects.get(id=course)     
        user.save()
        return redirect('teacher_page')

def logout(request):
    auth.logout(request)
    return redirect('load_page')






