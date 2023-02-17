from django.shortcuts import render,redirect ,HttpResponse
from .models import Student
from django.contrib.auth import logout ,authenticate,login
from django.contrib.auth.models import User
from .forms import AddStudentForm
from django.contrib import messages
# Create your views here.



def Home(request):
    stu_data= Student.objects.all()
    return render(request , 'core/home.html',{'studata':stu_data})


def Add_Student(request):
    print(request.user)
    if request.method == 'POST':    
        fm=AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request," You have successfully added a student")
            return redirect('/')
        else:
            return render(request,'core/add_student.html',{'form':fm})

    fm=AddStudentForm()
    if request.user.is_anonymous:
            print(request.user)
            return redirect("login") 
    return render(request,'core/add_student.html',{'form':fm})

def Delete_Student(request,id):
    if request.user.is_anonymous:
            print(request.user)
            return redirect("login")
    # if request.method == "POST":
        # data=request.POST
        # print(data)
        # id=data.get('id')
    studata = Student.objects.get(id=id)
    studata.delete()
    messages.warning(request," You have successfully deleted the student")
    return redirect("/")

def Edit_Student(request,id):
    if request.user.is_anonymous:
            print(request.user)
            return redirect("login")
    if request.method == "POST":
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(request.POST , instance=stu)
        if fm.is_valid():
            fm.save()
            messages.info(request," You have successfully edited the student")
            return redirect("/")
        else:
            return render(request,'core/edit_student.html',{'form':fm})

    print(id)
    stu = Student.objects.get(id=id)
    fm = AddStudentForm(instance=stu)
    return render(request,'core/edit_student.html',{'form':fm})
        
def Register(request):
    if request.method == "POST":
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
     
        if len(username) > 20:
            return redirect("/")

        if pass1!=pass2:
            return redirect("/")

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Congratulations !! Your account has been successsfully created")
        return redirect("login")
   
    
    return render(request , "core/register.html")

def Login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username , password = password)
        if user is not None:
            login(request , user)
            return redirect("/")
        else:
            messages.warning(request,"Oops !! You have entered wrong credientials")
            return redirect("login")   

    return render(request ,'core/login.html')

def Logout(request):
    logout(request)
    return redirect("/")





   