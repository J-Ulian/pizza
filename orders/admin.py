from django.contrib import admin

from .models import Pizza, Topping
# Register your models here.


class ToppingAdmin(admin.ModelAdmin):
    filter_horizontal = ("pizzas",)


class ToppingInline(admin.StackedInline):
    model = Topping.pizzas.through
    extra = 1


class PizzaAdmin(admin.ModelAdmin):
    inlines = [ToppingInline]


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Topping, ToppingAdmin)
