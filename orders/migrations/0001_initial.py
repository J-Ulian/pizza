# Generated by Django 3.0.6 on 2020-05-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=8)),
                ('option', models.IntegerField()),
                ('big_size', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=64)),
                ('pizzas', models.ManyToManyField(blank=True, related_name='toppings', to='orders.Pizza')),
            ],
        ),
    ]
