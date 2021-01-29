# CrudEmployeeSimple
berdasarkan video tutorial [disini](https://www.youtube.com/watch?v=N6jzspc2kds&list=PLVZjE_PlezICSdGDkJOvZyaMJ9qq5GM91&index=11&t=1598s)

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

    - static
        - copas jika sudah ada, jika belum buat folder:
        - folder css,scss,fonts,img,js
        - folder static_root
        - Registrasi static di core/settings.py:
            ```
            STATIC_URL = '/static/'
            STATIC_ROOT =  BASE_DIR / 'static','static_root'

            STATICFILES_DIRS = [
                BASE_DIR / 'static'
            ]
            ```

    - media
        - copas jika sudah ada, jika belum buat folder:
        - folder property, agents, contact, about
        - Registrasi media di core/settings.py:
            ```
            MEDIA_URL = '/media/'
            MEDIA_ROOT = BASE_DIR / 'media'
            ```

    - Membuat file requirements.txt
        - buat requirements.txt
        - pip freeze > requirements.txt
- Model
    - employee_register/models.py


- Templates
    - core.settings.py tidak perlu ada perubahan karena template buka di root:
        <!-- - Pastikan 'bootstrap4' sudah teregister
        - `'DIRS': ['templates'],` -->
    - employee_register/templates/employee_register
        - base.html
        - employee_list.html
        - employee_form.html

- Form
    - pip install django-crispy-forms
    - register pada core/settings.py:
    ```
        'crispy_forms'
    ```
    `CRISPY_TEMPLATE_PACK = 'bootstrap4'`
    - employee_register/form.py
- View
    - employee_register/view.py, code:
        - employee_list()
        - employee_form()
        - employee_delete()
        
- Routing url
    - core / urls.py
        - code:
        ```
        ```
    - employee_register / urls.py

- Menampilkan semua field di admin panel