from __future__ import unicode_literals
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, CreateNewList

from django.contrib.auth.decorators import login_required


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


def listik(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")
        return render(response, "orders/list.html", {"ls": ls})

    return render(response, "orders/home.html", {})


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


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            # adds the to do list to the current logged in user
            response.user.todolist.add(t)

            return HttpResponseRedirect("/%i" % t.id)

    else:
        form = CreateNewList()

    return render(response, "orders/create.html", {"form": form})


def view(response):
    return render(response, "orders/view.html", {})
