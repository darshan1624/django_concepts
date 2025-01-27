from django.shortcuts import render, redirect
from receipe.models import Receipe, StudentMarks
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Student
from django.core.paginator import Paginator
from django.db.models import Q, Sum

# Create your views here.
@login_required(login_url="/login/")
def receipe(request):
    if request.method == 'POST':
        receipe_name = request.POST.get('receipe_name')
        desc = request.POST.get('desc')
        image = request.FILES.get('receipe-image')
        print(receipe_name)
        print(image)
        x = Receipe.objects.create(receipe_name=receipe_name, desc=desc, image=image)


        return redirect('/receipe')
    
    all_receipes = Receipe.objects.all()

    search_query = request.GET.get('search_receipe') 
    if search_query:
        all_receipes = all_receipes.filter(receipe_name__icontains = search_query)

    context = {'all_receipes': all_receipes} 

    return render(request, 'receipe/receipe.html', context)

def delete(request, id):
    receipe_to_delete = Receipe.objects.all().get(id=id)
    receipe_to_delete.delete()
    return redirect('/receipe')

def update_receipe(request, id):
    receipe_to_update = Receipe.objects.get(id=id)
    if request.method == 'POST':
        receipe_name = request.POST.get('receipe_name')
        desc = request.POST.get('desc')
        image = request.FILES.get('receipe-image')
        receipe_to_update.receipe_name = receipe_name
        receipe_to_update.desc = desc
        if image:
            receipe_to_update.image = image
        receipe_to_update.save() 
        return redirect('/receipe')

    context = {'receipe_to_update':receipe_to_update}
    return render(request, 'receipe/update_receipe.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username):
            messages.error(request, 'User doesnt exists with this username.')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Please enter correct password.')
            return redirect('/login/')
        else:
            login(request, user)
            messages.success(request, 'Login successfully.')
            return redirect('/receipe/')

    return render(request, 'receipe/login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)

        # If we metions password in create it wont encrypt
        # If username is duplicate it will throw an error
        user =  User.objects.filter(username = username)
        if user.exists():
            messages.error(request, 'Error: User already exists.')
            return redirect('/register/')

        user = User.objects.create(
            username = username
        )

        # If we use set_password it will encrypt
        user.set_password(password)
        user.save()
        
        return redirect('/register/')
    return render(request, 'receipe/register.html')


def get_students(request):
    students = Student.objects.all()

    search = request.GET.get('search')
    if search:
        students = Student.objects.filter(
            Q(student_name__icontains = search) | Q(student_address__icontains = search) | Q(student_email__icontains = search) | Q(student_age__icontains = search) | Q(department__department__icontains = search) 
            )

    paginator = Paginator(students, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    total_pages = range(1,paginator.num_pages+1)

    context = {'page_obj':page_obj, 'total_pages':total_pages} 
    return render(request, 'receipe/student.html', context)

def see_marks(request, student_id):
    student_marks = StudentMarks.objects.filter(student__student_id__studentid = student_id)
    total_marks = student_marks.aggregate(Sum('marks'))['marks__sum']
    # ranks = Student.objects.annotate(total_marks = Sum('studentmarks__marks')).order_by('total_marks', 'student_age')
  

    # current_rank = -1
    # i = 1 
    # for rank in ranks:
    #     if student_id == rank.student_id.studentid:
    #         current_rank = i
    #         break   
    #     i = i + 1


    # context = {'student_marks':student_marks, 'total_marks':total_marks, 'rank':current_rank}
    context = {'student_marks':student_marks, 'total_marks':total_marks}
    return render(request, 'receipe/see_marks.html', context)




