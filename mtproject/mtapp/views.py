from django.shortcuts import render
from django.http import HttpResponse
from mtapp.forms import EmpForm,StudForm
from mtapp.models import Tech,Student
# Create your views here.


def index(request):
    return HttpResponse("hiii")

def emp_reg(request):
    if request.method=="GET":
        e=EmpForm()
        return render(request,"empreg.html",{'name':e})   
    else:
        frm=EmpForm(request.POST)
        if frm.is_valid():
            frm.save()
            print(frm)

        return HttpResponse("Successfuly submitted")
    
def tech_add(request):
    # return render (request,'image.html')
    if request.method=="POST":
        ad=request.POST.get("fname")
        dd=request.FILES["lname"]
        print(ad)
        print(dd)
        var=Tech.objects.create(first_name=ad,photo=dd)
        var.save()
        return HttpResponse("<script>window.alert('successfully added!...');window.location.href='/s_reg/'</script>")

    else:
     return render (request,'image.html')
    

def setsession(request):
    request.session["name"]="ammu"

    request.session["email"]="ammu@gmail.com"

    return HttpResponse("session set...!")

def getsession(request):
    n=request.session["name"]
    e=request.session["email"]
    return HttpResponse(n +"and"+ e)

def delsession(request):
    del request.session["name"]
    return HttpResponse("successfully deleted...!")

def setcook(request):
    res=HttpResponse("cookie set")
    res.set_cookie('name','ammu')
    return res

def getcook(request):
    b=request.COOKIES["name"]
    return HttpResponse(b)

def Studreg(request):
    if request.method=="GET":
        e=StudForm()
        return render(request,"register.html",{'name':e})   
    else:
        frm=StudForm(request.POST)
        
        if frm.is_valid():
            frm.save()
            print(frm)
            return HttpResponse("<script>window.alert('successfully added!...');window.location.href='/stud_reg/'</script>")


def stud_view(request):
    st=Student.objects.all()
    return render(request,'view.html',{'data':st})








