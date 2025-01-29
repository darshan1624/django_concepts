This project contains files that may explain the concepts learned via some course from youtube, udemy, etc. 

1) Send context to html page/template  (context ). Cretaed emplaoyee table in html template and passed employee details
2) used tags e.g. |truncatechars:80
3) if elif else in templates 
4) for loop in templates 
5) template inheritance (extends , blockbody, endblock) 

6) created a Student model. (always regiester model before performing migrations). Understood migrations and models. 
7) Used shell. Understood how to add, view data from model via shell. 

8) CRUD queries in django performed on model Car. 
    C:
    1)car = Car(name='Nexon', speed=20)
    car.save()
    2)Car.objects.create()
    3)car_dict = {name='Nexon', speed=20}
    Car.objects.create(**car_dict)

    R:
    1)Car.objects.all()
    2)Car.objects.get(id=1)
    3)Car.objects.filter(id=1)

    U:
    1)car= Car.objects.get(id=1) 
    car.name= 'Creta'
    car.speed= 200
    car.save()
    2)Car.objects.get(id=1).update(name='Creta')

    D:
    1)Car.objects.get(id=1).delete()
    Car.objects.all().delete()

9) Created a new app receipe. 
    1) Created a model receipe. (name, desc, image) 
    2) created a html page with form. 
    3) views.py setup. (used return redirect('/'). So, that form data doesnt reload).
    4) To handle media files, extra configuration done in settings.py (MEDIA_URL, MEDIA_ROOT) and urls.py. 
      This config allows to setup media url via which media files can be accesed. 
    5) Added html table to receipe page to view added receipes. 
    6) Added a delete button to delete added receipe. 
    7) Added a update button. created a webpage form to update receipe.
    8) Create a search bar. Used __icontains query filter.
    9) Created register form. 
        1) Used 'User' builtin in model. 
        2) Used .set_password() fucntion to encrypt password.  
        3) user.exits() to see if user exists.
        4) Used user.authenticate() to verify password
        5) Used user.login() to create session for the user 
        5) Created success,error dismissible prompts using bootstrap. Used django message framework.
        6) Used Logout() to remove session for the user 
        7) Used @login_decorator(login_url='/login/') to redirect to login page 
  
10) Django ORM queries. Created a model Bikes.
    a)   .order_by('receipe_view_count')            
    b)   .order_by('-receipe_view_count')     # for descending order put - sign  
    c)   If want to limit use slicing .order_by('-receipe_view_count')[0:10]
    d)   .filter(receipe_view_count = 55)
    e)   .filter(receipe_view_count__gte = 55)     # greater than or equal to 
    f)   .filter(receipe_view_count__lte = 55)

11) Generated fake data using faker library for models studentID, students. Used Random also to assign department. Create query in seed.py.   

12) Django QuerySet
    1) Student.objects.filter(student_name__startswith = 'an')
    2) Student.objects.filter(student_name__endswith = 'it')
    3) Student.objects.filter(student_name__icontains = 'ka')
    
    4) By default we have a primary key in models and can be found with id,pk.
    queryset = Student.objects.filter(student_name__icontains = 'ay')
    //Only on single object can be applied 
    queryset[0].id 
    queryset.first().pk

    5) With foreign key you can refrence/find all the column values of refrenced model (department).  
    queryset = Student.objects.filter(student_name__startswith = 'an')
    > queryset[0].department 
    ==> <Department: Comps> will return object since its a foreign key 
    > queryset[0].department.department
    ==> Will return value 'Comps'.
    > query_set[0].department.id ==> 1

    6) We can also refrence to forign key in query set 
    > Student.objects.filter(department__department = 'Comps')
    But if you do 
    > Student.objects.filter(department = 'Comps')
    ==> ValueError: Field 'id' expected a number but got 'Comps'.
    Beacuse, department in Student table is foreign key. 
    > Student.objects.filter(department = 1) ==> will work 

    if want to apply django function also 
    > Student.objects.filter(department__department__icontains = 'Co')

    7) Find all the students belongs to ELEC, CHEM.
    __in is used to iterate over list 
    > Student.objects.filter(department__department__in = ['ELEC', 'CHEM']) 

    8) Find all the students who do not belongs to ELEC
    > Student.objects.exclude(department__department = 'ELEC')

    9) queryset = Student.objects.exclude(department__department = 'ELEC')
    query_set.count()  //len(query_set) also works 
    ==> 88
    count of objects return from queryset. 

    10) query_set = Student.objects.filter(department__department__in = ['AERO'])
    query_set.exists()
    ==> False   //returns true when returns any object 

    11) Student.objects.filter(student_age = 21).values()
    this serializes the data or returns the data in dict form. Used when want to send data in json form 

    Aggregate Operations:
    // Only applied one column at a time.
    1) Student.objects.aggregate(Sum('student_age'))
    2) Student.objects.aggregate(Max('student_age'))
    3) Student.objects.aggregate(Min('student_age'))
    4) Student.objects.aggregate(Avg('student_age'))

    Annotate Operations: 
    // Used to perform aggregate on more than one column 
    1) Student.objects.values('student_age').annotate(Count('student_age'))
    annotate groupby on whatever column metioned in values() and perform Count for each group. 

13) Report Card proj:
    1) Create table Subject(subject)
    Create table SubjectMarks(subject, student, marks)
    foreign key (subject, student)
    used unique_together = ['student', 'subject']

    2) Add entries in SubjectMarks. Written logic in seed.py

    3) Writen view to to get students from Student table 
    Create html page to view Students 

    4) Implemented Pagination. Used library Paginator. 
    used functions .get_page(), .num_pages

    5) Created a search bar form, to query specific values from table. 
    Used Q (from django.db.models import Q) to apply multiple OR conditons on diff columns.

    6) Create a seperate html page to see_marks of individual student. Show subject, marks. Total marks (sum every subj), rank. Create view for same. Used aggregate to get total marks. 

    7) To find rank. first identified total marks of each student, using annotate. Then sorted marks in descending order, then used for loop with counter to indetify rank.
    Since, above appraoch requires rank to be indetifed each time, when someone looks for particular student marks.
    So, we stored rank in model Rank(student, student_rank, date_of_report_card_generation). 
    Created function student_ranks in seed.py to add ranks to each student. 
    Now once we have the id of student we can identify rank of the student. 

14) Custom User Model 
    Django provides two type of classes
    1) abstract user class   (django fields/Columns + new fileds)
    2) abstact baseuser class (create from scratch only will get username, password)

    Write model manager  
    So, that django know to create additonal field for user menitoned in customUser.
    Otherwise when u excute createuser it wont create other fields.

    To write model manager. Create new file manager.py in app (on level of views, models,..)
    from django.contrib.auth.base_user import BaseUserManager
    Create a class UserManger(BaseUserManager):

    Now just like creatsuperuser we have two other functions 
    1) create_user
    2) create super_user 

    customize both functions. 
    pass required params 
 
    In settings.py need to mention the customUser model you created. 

    AUTH_USER_MODEL = 'appname.CustomUser'

    //Now u may face import issues if already using defaul user model of django
    // in other views or other apps.

    To switch to customUser model for other apps, import customUser
    from django.contrib.auth import get_user_model 

    User = get_user_model()
