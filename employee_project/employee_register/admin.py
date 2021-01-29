from django.contrib import admin
from .models import Employee, Position
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    employee_display = ['fullname' , 'position']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position)
