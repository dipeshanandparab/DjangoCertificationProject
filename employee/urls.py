from django.urls import path
from .views import employeeList
from .views import employeeDetail
from .views import upload

urlpatterns = [
    path('', employeeList, name='Employee_List' ),
    path('<int:employee_id>/', employeeDetail, name='Employee_Detail' ),
    path('upload/', upload, name='Upload_Employee_Data' ),
]