# Generated by Django 3.0.6 on 2020-05-19 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('pizzas', models.ManyToManyField(blank=True, related_name='orders', to='orders.Pizza')),
            ],
        ),
    ]
