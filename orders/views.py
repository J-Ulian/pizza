from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza
# Create your views here.
def index(request):
    context = {
        "menu": Pizza.objects.all()
    }
    return render(request, "orders/index.html", context)
    #return HttpResponse("Project 3: TO DO")
