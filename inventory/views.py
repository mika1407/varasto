from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def display_laptops(request):
    items = Laptops.objects.all()
    context = {
        'items' : items,
        'header' : 'Laptops',
    }
    return render(request, 'index.html', context) # 3 arguments

def display_desktops(request):
    items = Desktops.objects.all()
    context = {
        'items' : items,
        'header' : 'Desktops',
    }
    return render(request, 'index.html', context) # 3 arguments

def display_mobiles(request):
    items = Mobiles.objects.all()
    context = {
        'items' : items,
        'header' : 'Mobiles',
    }
    return render(request, 'index.html', context) # 3 arguments

#ADD
def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form' : form})

def add_laptop(request):
    return add_item(request, LaptopForm)


def add_desktop(request):
    return add_item(request, DesktopForm)

def add_mobile(request):
    return add_item(request, MobileForm)

#Edit
def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})

def edit_laptop(request, pk):
    return edit_item(request, pk, Laptops , LaptopForm)

def edit_desktop(request, pk):
    return edit_item(request, pk, Desktops, DesktopForm)

def edit_mobile(request, pk):
    return edit_item(request, pk, Mobiles, MobileForm)

#Delete
def delete_laptop(request, pk):

    template = 'index.html'
    Laptops.objects.filter(id=pk).delete()

    items = Laptops.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_desktop(request, pk):

    template = 'index.html'
    Desktops.objects.filter(id=pk).delete()

    items = Desktops.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_mobile(request, pk):

    template = 'index.html'
    Mobiles.objects.filter(id=pk).delete()

    items = Mobiles.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
