from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

from .models import Pizza, Topping
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "menu": Pizza.objects.all(),
        "user": request.user
    }
    return render(request, "orders/index.html", context)
    # return HttpResponse("Project 3: TO DO")


def registration_view(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "orders/registration.html", {"form": form})


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials"})


def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})


def pizza(request, pizza_id):
    try:
        pizza = Pizza.objects.get(pk=pizza_id)
    except Pizza.DoesNotExist:
        raise Http404("Flight does not exist.")
    context = {
        "pizza": pizza,
        "toppings": pizza.toppings.all(),
        "non_toppings": Topping.objects.exclude(pizzas=pizza).all()
    }
    return render(request, "orders/pizza.html", context)


def order(request, pizza_id):
    try:
        topping_id = int(request.POST["topping"])
        topping = Topping.objects.get(pk=topping_id)
        pizza = Pizza.objects.get(pk=pizza_id)
    except Topping.DoesNotExist:
        return render(request, "orders/error.html", {"message": "No topping."})
    except Pizza.DoesNotExist:
        return render(request, "orders/error.html", {"message": "No pizza."})
    except KeyError:
        return render(request, "orders/error.html", {"message": "No selection."})

    topping.pizzas.add(pizza)
    return HttpResponseRedirect(reverse("pizza", args=(pizza_id,)))
