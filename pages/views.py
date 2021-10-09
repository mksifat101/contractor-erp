from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from contractor.models import Employee


@login_required(login_url='login')
def home(request):
    employee = Employee.objects.all()
    context = {
        'employee': employee
    }
    return render(request, 'contractor/employee.html', context)
