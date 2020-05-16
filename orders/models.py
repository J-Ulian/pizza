from django.db import models

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
