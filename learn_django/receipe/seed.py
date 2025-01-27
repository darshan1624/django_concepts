from faker import Faker 
fake = Faker()
import random 
from .models import * 
from django.db.models import Sum

def seed_db(n=10):
    try: 
        for i in range(0,n):
            dapartments_objs = Department.objects.all()
            random_index = random.randint(0, len(dapartments_objs)-1) 
            department = dapartments_objs[random_index]
            student_id = f'STU-0{random.randint(100,999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 30)
            student_address = fake.address()

            student_id_obj = StudentId.objects.create(studentid = student_id)

            Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address
            )
    except Exception as e:
        print(e)


def seed_StudentMarks():
    students = Student.objects.all()
    subjects = Subject.objects.all()
    for student in students:
        for subject in subjects:
            StudentMarks.objects.create(
                student = student,
                subject = subject, 
                marks = random.randint(0,100))

def student_ranks():
    ranks = Student.objects.annotate(total_marks = Sum('studentmarks__marks')).order_by('-total_marks', '-student_age')
  
    i = 1 
    for rank in ranks:
        Rank.objects.create(
            student = rank, 
            student_rank = i
            )
        i = i + 1



