from django.db import models
from django import forms


class projectmodel(models.Model):
    project=models.CharField(max_length=100)
    #project_number=models.IntegerField(null=True,max_digits=10)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.project
    





# Create your models here.
class TaskModel(models.Model):
    task=models.CharField(max_length=100)
    #taskproject = models.ForeignKey(projectmodel,null=True, on_delete=models.CASCADE)
    #project_number=models.IntegerField(null=True,max_digits=10)
    complete='Complete'
    pending='Pending'
    cancelled='cancelled'
    #isComplete=models.BooleanField(default=False)
    #isCancelled=models.BooleanField(default=False)
    #isPending=models.BooleanField(default=False)
    work=projectmodel.objects.all()
    a=(('',''),)
    for t in work:
        a=a+((t.project,t.project),)
    status=models.CharField(max_length=10,choices=[(complete,'Complete'),(pending,'Pending'),(cancelled,'Cancelled')],default=pending)
    projects=models.CharField(max_length=10,choices=a,default=complete)
    date=models.DateTimeField(auto_now_add=True)
    cost=models.DecimalField(null =False,max_digits=10,decimal_places=2)
    budget=models.DecimalField(null=False,max_digits=10,decimal_places=2)
    def __str__(self):
        return self.task
    
class report(models.Model):
    topic=models.CharField(max_length=100)
    content=models.TextField(max_length=800)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.topic
    
