from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from .models import Employee


def employeeList(request):
    employee_list = Employee.objects.all()
    context = {
        'employee_list':employee_list,
        'title': 'Employee | Employee List'}
    return render(request, 'employee/employee_list.html', context)

def employeeDetail(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        context = {
            'employee':employee,
            'title':'Employee | Details '
        }
    except Employee.DoesNotExist:
        raise Http404('Employee Does Not Exist')
    return render(request, 'employee/employee_details.html', context)

def upload(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('Employee_List')
        else:
            return HttpResponse('Error Saving Details.')
    else:
        form = EmployeeForm()
        context = {'form': form }
        return render(request, 'employee/upload.html', context)
