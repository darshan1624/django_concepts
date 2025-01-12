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

