# CrudEmployeeSimple
berdasarkan video tutorial [disini](https://www.youtube.com/watch?v=N6jzspc2kds&list=PLVZjE_PlezICSdGDkJOvZyaMJ9qq5GM91&index=11&t=1598s)

- Summary
    - Template : Bootstrap4
    - Model : PostgreSQL
    - views: Function Based Views & Class based views
    - Form : crispy forms
    - Fitur: Login user
    - Problem : belum ada form tanggal, image

- Clone repo dan venv
    - cd PYTHON_FOLDER
    - git clone https://github.com/ArisDjango/CrudEmployeeSimple.git
    - cd CrudEmployeeSimple
    - python -m venv venv
    - Set-ExecutionPolicy Unrestricted -Scope Process
    - & d:/TUTORIAL/PYTHON/CrudEmployeeSimple/venv/Scripts/Activate.ps1

- Instalasi Django
    - python.exe -m pip install --upgrade pip
    - pip install django


- Struktur django
    - admin-conf
        - django-admin startproject core
        - rename 'core' menjadi 'employee_project'
    - App:
        - cd employee_project
        - python manage.py startapp employee_register 
        - Registrasi app di core/settings.py:
            ```
                'employee_register'
            ```
- Implementasi postgresql-django
    - Instalasi di lokal (jika belum)
        - instal postgreSQL.exe
        - login sebagai super user: psql -U postgres -h localhost
        - \du -> untuk melihat data user saat ini
        - \l untuk melihat database list
    - Mengatur User/pass, Hak akses, membuat DB.
        ```
            CREATE DATABASE employee;
            CREATE USER aris;
            GRANT ALL ON DATABASE aris to "employee";
            ALTER USER aris PASSWORD 'aris1985';
            ALTER USER aris CREATEDB;
        ```
    - postgresql setting di django
        - core/settings.py
        - Tentukan engine = postgres (defaultnya sqlite), name, user, pass, host, port: 
        ```
            DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': BASE_DIR / 'employee',
            'USER': 'aris',
            'PASSWORD': 'aris1985',
            'HOST': 'localhost'
                }
            }
        ```
        - Pastikan konfigurasi diatas sesuai dengan data waktu instalasi Postgres

    - Membuat file requirements.txt
        - buat requirements.txt
        - pip freeze > requirements.txt
- Model
    - employee_register/models.py
        - Position() - id(pk), title
        - employee() - id(pk), fullname, emp_code, mobile, position(fk=Position())

- Form
    - pip install django-crispy-forms
    - register pada core/settings.py:
        ```
            'crispy_forms'
        ```
        `CRISPY_TEMPLATE_PACK = 'bootstrap4'`
    - employee_register/forms.py
        - EmployeeForm(forms.ModelForm)
            --> akses model employee, mengambil fieldnya, memberikan label

- Templates
    - core.settings.py tidak perlu ada perubahan karena template buka di root:
        <!-- - Pastikan 'bootstrap4' sudah teregister
        - `'DIRS': ['templates'],` -->
    - employee_register/templates/employee_register
        - base.html 
            - base header & footer
        - employee_form.html
            - Load base, crispy_forms
            - csrf token
            - Form submit method=POST, set data hasil post sebagai data forms --> form.fullname|as_crispy_field, dst
            - button SUBMIT --> data s
            - button EMPLOYEE LIST --> url 'employee_list'
        - employee_list.html
            - Load base
            - {for employee in employee_list}
            - button ADD --> url 'employee_insert'
            - icon EDIT --> url 'employee_update' employee.id
            - icon DELETE 
            -    --> csrf_token
            -        Forms submit method=POST
            -        action = url 'employee_delete' employee.id
            
- View
    - employee_register/view.py, code:
        - import:
            ```
                from django.shortcuts import render, redirect
                from .forms import EmployeeForm
                from .models import Employee
            ```
        - employee_list(request)
            - request semua data dari models
            - render = request, "employee_register/employee_list.html", context
            - kondisi diatas = _READ (list)_
        - employee_form(request, id=0)
            - jika: ada request GET (dari path url)
                - jika: id = 0,
                    - (contoh: 127.0.0.1/employee/)
                    - menampilkan EmployeeForm() --> dari forms.py
                    - kondisi diatas = _READ(blank form)_ --> karena id=0, maka menampilkan blank form
                - else: Punya id
                    - (contoh: 127.0.0.1/employee/1/)
                    - ambil pk=id, dan memasukkannya kedalam employee,
                    - kondisi diatas = _READ DETAIL_
                - return render = request + employee_form.html, form

            - else: ada request selain GET,
                - jika: id = 0,
                    - menampilkan EmployeeForm() dengan parameter request POST
                    - kondisi diatas = _INSERT/CREATE_ --> READ(blank form) + SUBMIT
                - else: mempunyai id,
                    - ambil pk=id, gunakan POST
                    - kondisi diatas = _UPDATE_
                - jika: format input valid,
                    - maka disimpan
                - return /employee/list
        - employee_delete()
        
- Routing url
    - core / urls.py
        - code:
        ```
            urlpatterns = [
            path('admin/', admin.site.urls),
            path('employee/',include('employee_register.urls')),
            ]

        ```
    - employee_register / urls.py
        - catatan:
            - path=''
                - artinya id=0
                - menggunakan logic views.employee_form
                - pada logic views, jika id=0 maka menampilkan form kosong
                - name='employee_insert' --> ada pada template/./employee_list.html--> button ADD / TAMBAH DATA
        - code:
        ```
            from . import views

            urlpatterns = [
                path('', views.employee_form, name='employee_insert'),
                path(`'<int:id>/'`, views.employee_form,name='employee_update'), 
                path('delete/`<int:id>`/',views.employee_delete,name='employee_delete'),
                path('list/',views.employee_list,name='employee_list') 
            ]
                    
        ```

        - Menampilkan semua field di admin panel


        =====================
1. Model --> field ORM
2. forms.py --> mengambil field model untuk diolah class baru, diberi label,

3. views.py --> mengambil class forms.py untuk diolah logic crud
    - READ (all) = render('request get' dari list.html yang melakukan 'for' terhadap data context/model)
    - FORM (blank)
    - READ (details)
    - INSERT / CREATE
    - DELETE

4. employee_form.html --> menampilkan form kosong jika id = 0, form update jika id=n (config di view)
                      --> menggunakan tag crispy forms untuk menangkap POST dari user
                      --> submit akan merubah nilai forms.py ( otomatis merubah nilai model)

5. employee_list.html --> 
