from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receipe(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    # models.CASCADE = delete all the receipes realted to the user
    # models.SET_NULL = sets value null if user is removed 
    # models.SET_DEFAULT = to set default value  
    receipe_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=800)
    image = models.FileField(upload_to='receipe/')

    def __str__(self):
        return self.receipe_name

class Bikes(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    bike_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=800)
    bike_mileage = models.IntegerField(default=20)
    image = models.FileField(upload_to='receipe/')

    def __str__(self):
        return self.bike_name


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department
    
    class Meta:
        ordering = ['department']

class StudentId(models.Model):
    studentid = models.CharField(max_length=100)

    def __str__(self):
        return self.studentid

class Student(models.Model):
    department = models.ForeignKey(Department, related_name='depart', on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentId, related_name='student_id',on_delete=models.CASCADE)

    student_name = models.CharField(max_length=200)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.CharField(max_length=800)

    def __str__(self):
        return self.student_name

    class Meta:
        ordering = ['student_name']
        verbose_name = 'Student1'


class Subject(models.Model):
    subject  = models.CharField(max_length=200)

    def __str__(self):
        return self.subject

class StudentMarks(models.Model):
    student = models.ForeignKey(Student, related_name='studentmarks', on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    marks = models.IntegerField()

    class Meta:
        unique_together = ['student', 'subject']
    
    def __str__(self):
        return f'student: {self.student}, subject: {self.subject}'


class Rank(models.Model):
    student = models.ForeignKey(Student, related_name = 'studentranks', on_delete = models.CASCADE)
    student_rank = models.IntegerField()
    date_of_report_card_generation = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['student_rank', 'date_of_report_card_generation']


