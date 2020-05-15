from django.db import models

# Create your models here.

class Toppings(models.Model):
    topping = models.CharField(max_length=24)

    def __str__(self):
        return f"{self.topping}"



class Pizza(models.Model):
    origin = models.CharField(max_length=8)
    toppings = models.IntegerField()
    topping = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name="includes", null=True)
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
                return f"{self.origin} Small Pizza with {self.toppings} topping(s) - {self.price}$"
            else:
                return f"{self.origin} Large Pizza with {self.toppings} topping(s) - {self.price}$"        
        
