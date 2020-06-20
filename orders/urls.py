from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.menu, name="menu"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("cart/", views.cart, name='cart'),
    path("add_order/", views.add_order, name='add_order'),
    path("fetch_orders/", views.fetch_orders, name="fetch_orders"),
    path("confirm_order/", views.confirm_order, name="confirm_order"),
    path("view_orders/", views.view_past_orders, name="view_orders"),
    path("view_customers_orders/", views.view_customers_orders, name="view_customers_orders"),
    path("pending_to_confirmed/", views.pending_to_confirmed, name='pending_to_confirmed')
]
