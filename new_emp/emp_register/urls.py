from django.urls import path,include
from .import views

urlpatterns = [

    path('',views.employee_form, name='emp_insert'), #get and post req. for insert operation
    path('<int:id>/',views.employee_form, name='emp_update'), # get and post req. for update operation
    path('<int:id>',views.employee_delete, name='emp_delete'),
    path('list/',views.employee_list, name='emp_list') # get req. retrieve and display all records
]