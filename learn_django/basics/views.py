from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    employees = [{'name':'amit', 'marks':20}, {'name':'anket', 'marks':40}, {'name':'anshuman', 'marks':10}, {'name':'yash', 'marks':60}]
    # this is called context, parmaetrs you pass to templates 
    context = {'employees':employees, 'page':'home'}
    return render(request, 'basics/home.html', context)

def about(request):
    employees = [{'name':'amit', 'marks':20}, {'name':'anket', 'marks':40}, {'name':'anshuman', 'marks':10}, {'name':'yash', 'marks':60}]
    
    text = """Lorem, ipsum dolor sit amet consectetur adipisicing elit. Mollitia rem nemo architecto accusamus eligendi, aut aliquid ex quam unde. Aliquam consequuntur dolor doloribus adipisci quaerat rerum facilis iure eius vel.
      Nisi dignissimos animi obcaecati. Esse quae quibusdam blanditiis atque iusto ut explicabo voluptatum, aut sed aperiam quia, optio eaque facilis deserunt. Commodi qui temporibus mollitia repudiandae aspernatur! Consequuntur, incidunt aliquam!
      Quia vel quo repellendus voluptatibus exercitationem eveniet officiis expedita itaque cumque, tempore aperiam, impedit sapiente accusantium? Quibusdam eius autem dolore rem accusamus reiciendis reprehenderit, totam repellat ullam numquam beatae! Magnam!
      Perferendis dolorum, nemo aliquam harum soluta a quibusdam omnis saepe adipisci? Tempora atque accusantium voluptatum laboriosam sint? Placeat aliquam, repudiandae ut voluptas molestiae itaque saepe assumenda, dicta, odio sit incidunt.
      Delectus perspiciatis pariatur ad praesentium, quam vel aliquam nostrum obcaecati hic cum, fuga odio, quod consequuntur. Vero quasi alias itaque odit maiores mollitia saepe distinctio, totam consequatur atque beatae at!"""

    context = {'employees':employees, 'page':'about', 'text':text}
    return render(request, 'basics/about.html', context)

def contact(request):
    employees = [{'name':'amit', 'marks':20}, {'name':'anket', 'marks':40}, {'name':'anshuman', 'marks':10}, {'name':'yash', 'marks':60}]
    context = {'employees':employees, 'page':'contact'}
    return render(request, 'basics/contact.html', context)

