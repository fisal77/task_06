from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "restaurants":Restaurant.objects.all()
    }
    return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
    context = {
        "restaurant": Restaurant.objects.get(id=restaurant_id)
    }
    return render(request, 'detail.html', context)

def restaurant_create(request):
    form = RestaurantForm()
    if request.method == "POST":                # if the posted form is POST not GET
        form = RestaurantForm(request.POST)     # then get the posted data fields
        if form.is_valid():                     # then check if fields are valid (filled)
            form.save()                         # then save it into database
            return redirect("restaurant-list")  # and return to main (previuos) page
    context = {
        "create_form":form
    }
    return render(request, 'create.html', context)
