from django.contrib import admin
from StudentDBApp.models import Student,Student2

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']
admin.site.register(Student,StudentAdmin);

from StudentDBApp.models import Student2
class Student2Admin(admin.ModelAdmin):
    list_display=['rollno', 'name', 'dob','marks','email', 'phonenumber','address']

admin.site.register(Student2,Student2Admin);


