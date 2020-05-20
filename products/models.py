# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    type_of_food = models.CharField(max_length=120, blank=True)
    name = models.CharField(max_length=120)
    option = models.CharField(max_length=120, blank=True)
    big_size = models.BooleanField(default=False, blank=True)
    price = models.FloatField(blank=True)

    def __str__(self):
        if self.price:
            return f"{self.name} {self.type_of_food} for {self.price}"
        else:
            return f"{self.name} {self.type_of_food}"
