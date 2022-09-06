from multiprocessing import context
from pyexpat import model
from django.forms import Form
from django.shortcuts import render,redirect
from . models import TaskModel,report
from . forms import TaskModelForm, TaskUpdateForm, reportform
from django.http import HttpResponse#import http.Response
# Create your views here.

def index(request):
    if request.method=='POST':#if there is a request to post
        form=TaskModelForm(request.POST)
        if form.is_valid():#if it meets all contraints. mine worked without the brackets
            form.save()
            return redirect('/')
    else:
        form=TaskModelForm()

    data=TaskModel.objects.all().order_by('-date')# the same as TaskModel.objects.raw('select * from "taskapp_Taskmodel" ')
    total_task=data.count()
    completed_task=TaskModel.objects.filter(status='Complete').count()
    pending_task=TaskModel.objects.filter(status='Pending').count()
    cancelled_task=total_task-(completed_task+pending_task)
    i=0
    total_budget=0
    total_cost=0
    
    for task in data:
        total_budget=total_budget+task.budget
        total_cost=total_cost+task.cost
    
    balance=total_budget-total_cost
        
    context={
        'data':data,
        'total_budget':total_budget,
        'balance':balance,
        'total_cost':total_cost,
        'form':form,
        'total_task':total_task,
        'completed_task':completed_task,
        'pending_task':pending_task,
        'cancelled_task':cancelled_task,
    }
    
    
    return render(request,"index.html",context)#loads the html file.passes in data from the modles file

def about(request):
    return render(request,"about.html")

def delete(request,pk):
    item=TaskModel.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/project')
    return render(request,"delete.html")

def edit(request,pk):
    item=TaskModel.objects.get(id=pk)

    if request.method=='POST':
        form=TaskUpdateForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/project')
    else:
        form=TaskUpdateForm(instance=item)


    context={
        'form':form
    }
    return render(request,'edit.html',context)

def reports(request):
    data=report.objects.all()
    if request.method=='POST':#if there is a request to post
        form=reportform(request.POST)
        if form.is_valid():#if it meets all contraints. mine worked without the brackets
            form.save()
            return redirect('/report')
    else:
        form=reportform()
    
    context={
        'data':data,
        'form':form,
    }

    return render(request,"reports.html",context)#loads the html file.passes in data from the models file

def edit_report(request,pk):
    item=report.objects.get(id=pk)

    if request.method=='POST':
        form=reportform(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/report')
    else:
        form=reportform(instance=item)
        
    context={
        'form':form,
    }
    return render(request,"editreport.html",context)

def delete_report(request,pk):
    item=report.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/report')
    return render(request,"delete.html")
    

def dashboard(request):
    return render(request,"dashboard.html")

"""
def index(request):
    return HttpResponse("HomePage")


def about(request):
    return HttpResponse("About Page")
"""