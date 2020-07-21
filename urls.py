from django.urls import path

from . import views

urlpatterns = [ 
    path("", views.index, name="index"),
    path("product/single_product/<slug:slug>", views.single, name="single"),
    path("cart/", views.cart, name="cart")     

]