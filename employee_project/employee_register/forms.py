from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm): # model dari forms disini ada di venv

    class Meta: # Meta: class khusus untuk memanggil model, dibutuhkan ModelForm
        model = Employee
        fields = ('fullname','mobile','emp_code','position') #--> tuple jadi param *args
        labels = {                                           #--> dict jadi param **kwargs
            'fullname':'Nama Lengkap',
            'mobile' : 'No. HP',
            'position' : 'Posisi',
            'emp_code':'EMP. Code',
            
        }

    # dipanggil pertama kali
    # param *args = tuple, **kwargs = dict
    def __init__(self, *args, **kwargs): 
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Pilih"
        self.fields['emp_code'].required = False