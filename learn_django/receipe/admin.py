from django.contrib import admin

# Register your models here.
from .models import Receipe, Bikes, Department, Student, StudentId

admin.site.register(Receipe)
admin.site.register(Bikes)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentId)


