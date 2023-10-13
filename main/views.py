from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from main.forms import ProductForm
from main.signupforms import SignUpForm
from django.urls import reverse
from main.models import Product
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import datetime


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    jumlah_item = products.count()

    context = {
        'name': request.user.username, # Nama kamu
        'class': 'PBP A', # Kelas PBP kamu
        'jumlah_item' : jumlah_item,
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

@csrf_exempt
def add_product_ajax(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        category = request.POST.get("category")
        platform = request.POST.get("platform")
        amount = request.POST.get("amount")
        user = request.user

        new_product = Product(name=name, price=price, description=description, category=category, platform=platform, amount=amount, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def delete_product_ajax(request,id):
    if request.method == "DELETE":
        item = Product.objects.get(pk = id)
        item.delete()

        return HttpResponse(b"DELETED", status=201)
    
    return HttpResponseNotFound()
        

def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type = "application/json")

def show_xml_by_id(request,id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request,id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def delete_data(request, id):
    data = Product.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def increase_amount(requet, id):
    data = Product.objects.get(pk=id)
    data.amount += 1
    data.save()
    return HttpResponse(b"UPDATE", status=201)

def decrease_amount(request,id):
    data = Product.objects.get(pk=id)
    if (data.amount > 0):
        data.amount -= 1
    else:
        data.amount = 0
    data.save()
    return HttpResponse(b"UPDATE", status=201)
