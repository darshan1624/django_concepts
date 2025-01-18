from django.contrib import admin

# Register your models here.
from .models import Receipe, Bikes, Department, Student, StudentId, Subject, StudentMarks

admin.site.register(Receipe)
admin.site.register(Bikes)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentId)
admin.site.register(Subject)

# column wise diplay in admin pannel
class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']


admin.site.register(StudentMarks, SubjectMarksAdmin)




