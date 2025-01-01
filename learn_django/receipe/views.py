from django.shortcuts import render, redirect
from receipe.models import Receipe
from django.http import HttpResponse

# Create your views here.

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
