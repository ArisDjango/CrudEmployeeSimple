from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'), # employee_insert  dipanggil oleh employee_list.html. get and post req. for insert operation
    path('<int:id>/', views.employee_form,name='employee_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('list/',views.employee_list,name='employee_list') # get req. to retrieve and display all records
]

# penjelasan hubungan dengan view
# path '' --> http://127.0.0.1:8000/employee/
#             Eksekusi: 'views.employee_form', request url metode GET, dengan kondisi: id = 0
#             Maka merender link 'employee_form.html',
#             id =0 maka menampilkan form kosong --> fitur READ-FORM/BLANK
#             Form diisi user,  lalu:
#             Button SUBMIT --> fitur INSERT/CREATE,
#                           --> otomatis merequest POST, (merubah logic di view jd else) menyimpan hasil post user ke form.py-, mempengaruhi model
#                           --> redirect ke employee_list.html (karena setelah POST form dg (id=0), akan memenuhi return, yaitu redirect )
#             Button LIST --> Redirect ke employee_list.html
#             'employee_insert'--> nama path ini, ada di employee_list.html<button ADD> ntuk redirect ke hal ini (form kosong)

# path '<int:id>/' --> http://127.0.0.1:8000/employee/1/
#             Eksekusi: 'views.employee_form', request url metode GET, dengan kondisi: id = n
#             Maka merender link employee_form.html,
#             id =n maka menampilkan form data dari id 'n' --> fitur READ-DETAIL
#             Form diubah user, lalu: 
#             Button SUBMIT   --> fitur UPDATE
#                             --> otomatis merequest POST (merubah logic di view jd else) menyimpan perubahan ke form.py-, mempengaruhi model
#                             --> redirect ke employee_list.html (karena setelah form terisi, akan memenuhi return, yaitu redirect )
#             Button LIST --> Redirect ke employee_list.html
#             'employee_update'--> nama path ini, ada di employee_list.html<button EDIT>, ada di tiap list untuk redirect ke hal ini (data detail)

# path 'delete/<int:id>' --> tidak merender halaman khusus
#             Eksekusi: 'views.employee_delete', request url metode GET, dengan kondisi: id = n
#             sebagai action form delete di employee_list.html,
#             id =n maka menghapus form data dari id 'n' --> fitur DELETE
#             user memilih data dari list, lalu: 
#             

# path 'list/' --> http://127.0.0.1:8000/employee/list
#             Eksekusi: 'views.employee_list', request url metode GET,
#             sebagai halaman utama employee_list.html,
#             memilih semua data dari model, dan menampilkannya
#             button UPDATE[n] redirect ke path '<int:id>/' --> http://127.0.0.1:8000/employee/1/
#             Button DELETE[n] --> fitur DELETE
#                              --> otomatis merequest POST, menyimpan perubahan hapus ke form.py-, mempengaruhi model
#                              --> redirect/tetap ke employee_list.html