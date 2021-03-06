# Generated by Django 3.0.7 on 2020-06-17 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200617_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='topping',
            field=models.ManyToManyField(blank=True, related_name='pizzas', to='orders.Topping'),
        ),
    ]
