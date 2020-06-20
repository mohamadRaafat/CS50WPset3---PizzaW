from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Pizza, Sub, Pasta, Salad, DinnerPlatter, CheckoutOrders
from .helpers import get_price
from datetime import datetime

# list to contain a dict with all values for every order
orders = []

# Create your views here.
def index(request):
    return render(request, "orders/index.html")

def menu(request):
    context = {
        "regular_pizzas": Pizza.objects.filter(type='Regular'),
        'sicilian_pizzas': Pizza.objects.filter(type='Sicilian'),
        'subs': Sub.objects.all(),
        'pastas': Pasta.objects.all(),
        'salads': Salad.objects.all(),
        "platters": DinnerPlatter.objects.all()
    }
    if request.user:
        context["user"] = request.user
    return render(request, "orders/menu.html", context)

def about(request):
    return render(request, "orders/about.html")

def contact(request):
    return render(request, "orders/contact.html")

def cart(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": "You must be logged in to view the cart"})
    return render(request, "orders/cart.html")

def add_order(request):
    
    global orders
    if request.method == 'POST':
        # get the price of the item
        price = get_price(request)

        if request.POST.get('extra'):
            price += 0.50

        orders.append({
            "name": request.POST.get('name'),
            "type": request.POST.get('type'),
            "topping": request.POST.get('topping'),
            "size": request.POST.get('size'),
            "number": request.POST.get('number'),
            "extra": request.POST.get('extra'),
            "price": price * float(request.POST.get('number'))
        })
        
        # remove any 'None" value along with its key from each dict inside orders list
        # so that the data passed will only be the required data
        orders = [{key: val for key, val in order.items() if val != None} for order in orders]

        # for index, order in enumerate(orders):
        #     print(f"===========================")
        #     print(f"order {index+1}")
        #     print(f"===========================")
        #     for key, value in order.items():
        #         print(f"{key}: {value}")

        return HttpResponseRedirect(reverse(menu))


# i'll use this view to fetch all the orders after an order is added to cart, then send the data ...
# using AJAX to js to be stored in localstorage
def fetch_orders(request):
    return JsonResponse(orders, safe=False)


@csrf_exempt
def confirm_order(request):
    if request.method == 'POST':
        try:
            order_details = request.POST.get('order_details_html')
            CheckoutOrders(ordered_by=request.user, order_details=order_details,date=datetime.utcnow()).save()
            # clear all the items from the cart after confirming checkout
            global orders
            orders = []
        except:
            pass
        return HttpResponseRedirect(reverse("menu"))

def view_past_orders(request):
    # get the orders of the logged in user
    all_orders = CheckoutOrders.objects.filter(ordered_by=request.user)
    return render(request, "orders/view_orders.html", {"all_orders": all_orders})


def view_customers_orders(request):
    # get ALL the confirmed orders, pending
    all_orders = CheckoutOrders.objects.filter(confirmed_by_restaurant=False)
    return render(request, "orders/view_customers_orders.html", {"all_orders": all_orders})


def pending_to_confirmed(request):
    order_id = request.POST.get('id')
    order = CheckoutOrders.objects.get(pk=order_id)
    order.confirmed_by_restaurant = True
    order.save()

    return HttpResponseRedirect(reverse("view_customers_orders"))
 
def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("menu"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid Credentials."})
    else:
        return render(request, "orders/login.html")

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "logged out."})

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        if not username or not firstname or not lastname or not email or not password:
            return render(request, "orders/register.html", {"message": "All fields are required"})
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        print(username, firstname, lastname, email, password)
        return render(request, "orders/login.html", {"message": "New user registered. Please login to proceed."})
    else:
        return render(request, "orders/register.html")
