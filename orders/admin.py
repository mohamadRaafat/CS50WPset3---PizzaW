from django.contrib import admin

from .models import Pizza, Topping, Sub, ExtraForSub, Pasta, Salad, DinnerPlatter, CheckoutOrders

# Register your models here.
admin.site.register(Pizza)  
admin.site.register(Topping)

admin.site.register(Sub)
admin.site.register(ExtraForSub)

admin.site.register(Pasta)
admin.site.register(Salad)

admin.site.register(DinnerPlatter)

admin.site.register(CheckoutOrders)
