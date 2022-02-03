from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student, Department, Register, Staff
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'college/home.html')

def application(request):
    return render(request, 'college/application.html')

def save(request):
    Student.objects.create(student_name=request.POST['name'], student_email=request.POST['Email'],
                           student_phone=request.POST['Phone'],father_name=request.POST['Father_name'],
                            course=request.POST['Course'],ssc_marks=request.POST['ssc_marks'],
                           inter_marks=request.POST['inter_marks'])
    return HttpResponseRedirect('/college/')



def registration(request):
    deps = Department.objects.all()
    return render(request, 'college/registration.html',{"deps": deps})


def save_details(request):
    if Student.objects.filter(student_email=request.POST['email'], is_verified=True).exists():
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        student = Student.objects.get(student_email=request.POST["email"])
        dep = Department.objects.get(code=request.POST['code'])
        Register.objects.create( image=request.FILES['image'], department=dep, user=user,Student=student)

        return HttpResponseRedirect('/college/')
    else:
        return render(request, 'college/application.html', {'error': 'you are not a valid user'})


def login_user(request):
    return render(request, 'college/login.html')


def validate(request):
    username= request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if User is not None:
        login(request, user)
        return HttpResponseRedirect('/college/details/')
    else:
        return render(request, 'college/login.html', {'error': 'Invalid username or password'})


@login_required(login_url="/college/login/")
def details(request):
    # import pdb
    # pdb.set_trace()
    #pdb.set_trace()
    user = request.user
    return render(request, 'college/details.html', {'user':user})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/college/login/')



def staff_registration(request):
    deps = Department.objects.all()
    return render(request, 'college/staff.html',{"deps": deps})


def save_staffdetails(request):
    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
    Register.objects.create(staff_name=request.POST['name'], staff_email=request.POST['email'],
                         staff_phone=request.POST['phone'], qualification=request.POST['qualification'],
                         staff_department=Department.objects.get(code=request.POST['code'],
                         experience=request.POST['experience'], image=request.FILES['image'], user=user))
    return HttpResponseRedirect('/college/')


def staff_validate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

        if Staff.objects.filter(user=user).exists():
            return HttpResponseRedirect('/college/staff_details/')
    else:
        return render(request, 'college/staff.html', {'error': 'you are not a valid user'})



def staff_login(request):
    return render(request, 'college/staff_login.html')


@login_required(login_url='/college/staff_login.html')
def staff_detail(request):
    user = request.user
    return render(request, 'college/staff_details.html', {'user': user})


def staff_logout(request):
    logout(request)
    return HttpResponseRedirect('/college/staff_login/')


@login_required(login_url="/college/staff_login/")
def total_staff(request):
    staff = Staff.objects.all()
    return render(request, 'college/totalstaff.html', {'staff': staff})

@login_required(login_url="/college/login/")
def total_students(request):
    deps = Department.objects.all()
    return render(request, 'college/totalstudents.html', {"deps": deps})


def std_details(request, dep_code):
    student = Register.objects.filter(department__code=dep_code)
    return render(request, 'college/mechstudents.html', {'student': student})



