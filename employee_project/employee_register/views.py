from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.


# READ

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}# employee_list diambil oleh list.html untuk perulangan 'for', sehingga isi model dapat muncul di html
    return render(request, "employee_register/employee_list.html", context) # request = GET dari halaman html dengan data dinamis dari context

# FORM
# jika : ada request GET (dari url)
#   jika: id = 0 --> menampilkan EmployeeForm()--> form kosong dengan field dari model (FORM)
#   else: mempunyai id --> buat var employee = model Employee-->ambil pk=id, 
#                           buat var form dengan nilai EmployeeForm(parameter employee(diatas))
#                           ex: 127.0.0.1/employee/1 --> (READ:DETAIL)
#   return render = menampilkan request GET dari employee_form.html berupa form(diatas)

# else: ada request selain GET, 
#   jika: id = 0 --> menampilkan EmployeeForm() dengan parameter request POST --> INSERT/CREATE
#           --> SUBMIT button menggunakan method post
#   else: mempunyai id, ambil pk=id, gunakan POST --> UPDATE
#   jika: format input valid, maka disimpan
#   return /employee/list
def employee_form(request, id=0): 
    if request.method == "GET":
        if id == 0: # ----------------------> READ - FORM BLANK
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id) # ---> READ - DETAILS
            form = EmployeeForm(instance=employee) 
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0: # --------------------------------> INSERT / CREATE
            form = EmployeeForm(request.POST)
        else:# ---------------------------------------> UPDATE
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

# DELETE
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')

# Create your views here.
