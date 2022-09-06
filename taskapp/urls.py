#created by user
from django.urls import path
from . import views

urlpatterns=[
    path('',views.dashboard,name='taskapp-dashboard'),
    path('project/',views.index,name='taskapp-index'),#shows landing page,calls index function in views
    path('about/',views.about,name='taskapp-about'),
    path('delete/<int:pk>/',views.delete,name="taskapp-delete"),
    path('edit/<int:pk>/',views.edit,name="taskapp-edit"),
    path('report/',views.reports,name="taskapp-report"),
    path('edit-report/<int:pk>/',views.edit_report,name="report-edit"),
    path('delete-report/<int:pk>/',views.delete_report,name="report-delete"),

]