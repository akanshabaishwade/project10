from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name="student_list"),
    path('Add_student', views.Add_student, name="Add_student"),
    path('delete/<int:id>/', views.delete, name="delete"),


]
