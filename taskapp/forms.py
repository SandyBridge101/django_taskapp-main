from asyncio import tasks
from dataclasses import field
from pyexpat import model
from django import forms
from .models import TaskModel,report

class TaskModelForm(forms.ModelForm):#for save
    class Meta:
        model=TaskModel
        fields=['task','budget','cost','projects']

class TaskUpdateForm(forms.ModelForm):#for edit
    class Meta:
        model=TaskModel
        fields='__all__'
        
class reportform(forms.ModelForm):#for edit
    class Meta:
        model=report
        fields='__all__'
        
