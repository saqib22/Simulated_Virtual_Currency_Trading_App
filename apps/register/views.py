from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . import models

def signup(request):
    return render(request, 'register/signup.html')

def register(request):
    #errors = User.objects.validator(request.POST)
    #if len(errors):
     #   for tag, error in errors.iteritems():
      #      messages.error(request, error, extra_tags=tag)
       # return redirect('/')

    #hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    #user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
    #user.save()
    #request.session['id'] = user.id
    return redirect('/success')

def login(request):
    if (models.User.objects.filter(name=request.POST['name'])):
        user = models.User.objects.filter(name=request.POST['name'])[0]
        request.session['id'] = user.id
        return redirect('/success')
    user = models.User.objects.create(name = request.POST['name'], deposit_amount = int(request.POST['amount']))
    user.save()
    request.session['id'] = user.id
    return redirect('/success')

def success(request):
    user = models.User.objects.get(id=request.session['id'])
    currency = models.VGC.objects.first()
    context = {
        "user": user,
        "currency" : currency
    }
    return render(request, 'register/success.html', context)