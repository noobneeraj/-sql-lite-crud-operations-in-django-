from django.shortcuts import render,redirect,HttpResponse
from .models import Student
from django.contrib import messages



# Create your views here.
def index(request):
    data=Student.objects.all()
    context={"data":data}

    return render(request,'index.html',context)

def insert(request):
    if request.method =='POST':
        name=request.POST.get('name')        
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,gender,age,email)
        query=Student(name=name,email=email,age=age,gender=gender)
        messages.info(request,'Student details inserted Sucessfully')
        query.save()

    return redirect('/')
    return render(request,'index.html')


def updateData(request,id):
    if request.method =='POST':
        name=request.POST.get('name')        
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.age=age
        edit.gender=gender
        edit.email=email
        edit.save()
        messages.warning(request,'Student details Updated Sucessfully')
        
        return redirect('/')
    d=Student.objects.get(id=id)
    context={"d":d}

    return render(request,'update.html',context)

def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    messages.error(request,'Student details Deleted Sucessfully')
    return redirect('/')
    

    return render(request,'delete.html',context)