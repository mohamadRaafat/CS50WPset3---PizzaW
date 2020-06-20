from django.db import models


types = (
    ('Regular', 'Regular'),
    ('Sicilian', 'Sicilian')
)

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name}"



class Pizza(models.Model):
    type = models.CharField(max_length=12, choices=types)
    description = models.CharField(max_length=25)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4 ,decimal_places=2)
    image_url = models.TextField()
    topping = models.ManyToManyField(Topping, blank=True, related_name='pizzas')

    def __str__(self):
        return f"{self.type} - {self.description}"



class ExtraForSub(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class Sub(models.Model):
    name = models.CharField(max_length=25)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.TextField()
    extras = models.ManyToManyField(ExtraForSub, blank=True, related_name="subs")

    def __str__(self):
        return self.name


class Pasta(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.price}"


class Salad(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.price}"

class DinnerPlatter(models.Model):
    name = models.CharField(max_length=25)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.TextField()

    def __str__(self):
        return self.name

class CheckoutOrders(models.Model):
    order_id = models.AutoField(primary_key=True)
    ordered_by = models.CharField(max_length=25)
    order_details = models.TextField()
    confirmed_by_restaurant = models.BooleanField(default=False)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.ordered_by} - {self.confirmed_by_restaurant} - {self.date}"
