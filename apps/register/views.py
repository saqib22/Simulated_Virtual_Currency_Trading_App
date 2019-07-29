from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from models import User

def signup(request):
    return render(request, 'register/signup.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')

def login(request):
    if (User.objects.filter(name=request.POST['name'])):
        user = User.objects.filter(name=request.POST['name'])[0]
        request.session['id'] = user.id
        return redirect('/success')
    user = User.objects.create(name = request.POST['name'], deposit_amount = int(request.POST['amount']))
    user.save()
    request.session['id'] = user.id
    return redirect('/success')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'register/success.html', context)