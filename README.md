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