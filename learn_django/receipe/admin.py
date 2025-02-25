from django.contrib import admin

# Register your models here.
from .models import Receipe, Bikes, Department, Student, StudentId, Subject, StudentMarks, Rank
from django.db.models import Sum

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

class RankAdmin(admin.ModelAdmin):
    list_display = ['student', 'student_rank', 'total_marks', 'date_of_report_card_generation']
    ordering = ['student_rank']
    def total_marks(self, obj):
        print('test2',obj.student)
        subject_marks = StudentMarks.objects.filter(student = obj.student)
        print('test1',subject_marks)
        marks = subject_marks.aggregate(marks = Sum('marks'))
        print('test',marks)
        return marks['marks']

admin.site.register(Rank, RankAdmin)




