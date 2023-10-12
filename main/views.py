import datetime
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from main.forms import ItemForm, Item
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/login')

def items(request) :
    books = Item.objects.filter(user=request.user)

    total_book = sum([book.amount for book in books])
    
    context = {
        'application' : 'Library Inventories',
        'name' : request.user.username,
        'class' : 'PBP - A',
        'books' : books,
        'total_book' : total_book,
        'last_login' : request.COOKIES['last_login'],
    }
    
    return render(request, 'items.html', context)

def book_views(request):
    books = Item.objects.filter(user=request.user)

    context = {
        'name' : request.user.username,
        'class' : 'PBP - A',
        'books': books,
    }

    return render(request, 'books.html', context)

# Fungsi form peminjaman buku
def added_books(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        books = form.save(commit=False)
        books.user = request.user
        books.save()
        return HttpResponseRedirect(reverse('main:items'))
    
    context = {'form' : form}
    return render(request, "added_books.html", context)

# Fungsi untuk mengubah data dalam XML
def show_xml(request):
    data = Item.objects.all()
    
    return HttpResponse(serializers.serialize("xml", data), content_type='application/xml')

# Fungsi untuk mengubah data dalam JSON
def show_json(request):
    data = Item.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Fungsi untuk mengambil data XML sesuai ID
def xml_by_id(request, id):
    data = Item.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Fungsi untuk mengambil data JSON sesuai ID
def json_by_id(request, id):
    data = Item.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:items")) 
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

def add_stock(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.amount += 1
    item.save()
    return redirect('main:books')

def reduce_stock(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if item.amount > 0:
        item.amount -= 1
        item.save()
    return redirect('main:books')

def edit_books(request, item_id):
    books = Item.objects.get(pk=item_id)

    form = ItemForm(request.POST or None, instance=books)

    if form.is_valid() and request.method == 'POST' :
        form.save()
        return HttpResponseRedirect(reverse('main:items'))
    
    context = {'form': form}
    return render(request, "edit_books.html", context)

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return redirect('main:books')

def get_book_json(request):
    books_item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', books_item))

@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        category = request.POST.get("category")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_book = Item(name=name, category=category, amount=amount, description=description, user=user)
        new_book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()