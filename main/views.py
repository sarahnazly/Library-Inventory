from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from main.forms import ItemForm, Item
from django.urls import reverse
from django.shortcuts import render

# Create your views here.
def items(request) :
    books = Item.objects.all()

    total_book = sum([book.amount for book in books])
    
    context = {
        'application' : 'Library Inventories',
        'name' : 'Sarah Nazly Nuraya',
        'class' : 'PBP - A',
        'books' : books,
        'total_book' : total_book,
    }
    
    return render(request, 'items.html', context)

# Fungsi form peminjaman buku
def borrow_books(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponseRedirect(reverse('main:items'))
    
    context = {'form' : form}
    return render(request, "borrow_books.html", context)

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