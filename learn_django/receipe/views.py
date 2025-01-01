from django.shortcuts import render, redirect
from receipe.models import Receipe

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

    return render(request, 'receipe/receipe.html')