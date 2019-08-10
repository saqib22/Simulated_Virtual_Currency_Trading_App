from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . import models
import decimal

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
    user = models.User.objects.create(name = request.POST['name'], deposit_amount = decimal.Decimal(request.POST['amount']))
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

def buying_transaction(request):
    currency = models.VGC.objects.first()
    user = models.User.objects.get(id=request.session['id'])

    if (request.POST.get('method') == 'market'):
        amount = request.POST['amount']
        total = (decimal.Decimal(amount) * currency.price)
        currency.amount = currency.amount - total
        user.deposit_amount = user.deposit_amount + total

    elif (request.POST.get('method') == "limit"):
        amount = request.POST['amount']
        price = request.POST['limitPrice']
        total = (decimal.Decimal(amount) * decimal.Decimal(price))
        currency.amount = currency.amount - total
        user.deposit_amount = user.deposit_amount + total

    currency.save()
    user.save()
    return redirect('/success')

def selling_transaction(request):
    currency = models.VGC.objects.first()
    user = models.User.objects.get(id=request.session['id'])

    if (request.POST.get('smethod') == 'smarket'):
        amount = request.POST['samount']
        total = (decimal.Decimal(amount) * currency.price)
        currency.amount = currency.amount + total
        user.deposit_amount = user.deposit_amount - total

    elif (request.POST.get('smethod') == "slimit"):
        amount = request.POST['samount']
        price = request.POST['slimitPrice']
        total = (decimal.Decimal(amount) * decimal.Decimal(price))
        currency.amount = currency.amount + total
        user.deposit_amount = user.deposit_amount - total

    currency.save()
    user.save()
    return redirect('/success')