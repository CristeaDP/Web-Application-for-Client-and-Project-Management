
from django.shortcuts import render, redirect, get_object_or_404
from .models import Shops, Persons,Memberships
from .forms import ShopForm, PersonForm, MembershipForm

def display_data(request):
    context = {
        'shops':Shops.objects.all(),
        'proiecte':Persons.objects.all(),
        'clienti_proiecte':Memberships.objects.all(),
        }
    return render(request, 'display_data.html',context)

def home(request):
    return render(request, 'home.html')
def add_shop(request):
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_shop")
    else:
        form = ShopForm()

    return render(request, "add_shops.html", {"form": form})


def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_person")
    else:
        form = PersonForm()

    return render(request, "add_person.html", {"form": form})

def add_membership(request):
    if request.method == "POST":
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_membership")
    else:
        form = MembershipForm()

    return render(request, "add_membership.html", {"form": form})

def manage_database(request):
    shops = Shops.objects.all()
    persons = Persons.objects.all()
    memberships = Memberships.objects.all()
    return render(request, 'manage_database.html', {
        'shops': shops,
        'persons': persons  ,
        'memberships': memberships
    })

def delete_shop(request, id):
    shops = get_object_or_404(Shops, id_shop = id)
    shops.delete()
    return redirect('display_data')

def delete_person(request, id):
    person = get_object_or_404(Persons, id_person = id)
    person.delete()
    return redirect('display_data')

def delete_membership(request, id):
    membership = get_object_or_404(Memberships, id_membership=id)
    membership.delete()
    return redirect('manage_database')

def modify_data(request):
    shops = Shops.objects.all()
    persons = Persons.objects.all()
    memberships = Memberships.objects.all()
    return render(request, 'modify_data.html', {
        'shops': shops,
        'persons': persons,
        'memberships': memberships
    })

def edit_shop(request, id):
    shop = get_object_or_404(Shops, id_shop=id)
    form = ShopForm(request.POST or None, instance=shop)
    if form.is_valid():
        form.save()
        return redirect('display_data')
    return render(request, 'edit_form.html', {'form': form})

def edit_person(request, id):
    person = get_object_or_404(Persons, id_person=id)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('display_data')
    return render(request, 'edit_form.html', {'form': form})

def edit_membership(request, id):
    membership = get_object_or_404(Memberships, id_membership = id)
    form = MembershipForm(request.POST or None, instance = membership)
    if form.is_valid():
        form.save()
        return redirect('display_data')
    return render(request, 'edit_form.html', {'form': form})