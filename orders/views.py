from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Pizza, Topping
# Create your views here.


def index(request):
    context = {
        "menu": Pizza.objects.all()
    }
    return render(request, "orders/index.html", context)
    # return HttpResponse("Project 3: TO DO")


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
