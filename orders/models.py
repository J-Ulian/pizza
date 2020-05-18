from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pizza(models.Model):
    origin = models.CharField(max_length=8)
    option = models.IntegerField()
    big_size = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        if(self.toppings == 0):
            if(self.big_size == False):
                return f"{self.origin} Small Pizza with cheese - {self.price}$"
            else:
                return f"{self.origin} Large Pizza with cheese - {self.price}$"
        else:
            if(self.big_size == False):
                return f"{self.origin} Small Pizza with {self.option} topping(s) - {self.price}$"
            else:
                return f"{self.origin} Large Pizza with {self.option} topping(s) - {self.price}$"


class Topping(models.Model):
    topping = models.CharField(max_length=64)
    pizzas = models.ManyToManyField(Pizza, blank=True, related_name="toppings")

    def __str__(self):
        return f"{self.topping}"


class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="todolist", null=True)  # <--- added
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
