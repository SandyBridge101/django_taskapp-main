from django.contrib import admin
from . models import TaskModel,report,projectmodel
# Register your models here.
"""
class TaskModelAdmin(admin.ModelAdmin):
    list_display=('task','date','isComplete')
"""
admin.site.register(TaskModel)
admin.site.register(report)
admin.site.register(projectmodel)

