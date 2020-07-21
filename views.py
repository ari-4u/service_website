from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):

  products = Product.objects.all()
  context = {'products':products}

  return render(request, "index.html", context)

def single(request, slug):

  products = Product.objects.filter(slug=slug)
  context = {'products':products}

  return render(request, "single.html", context)

def cart(request):

  return render(request, "cart.html")
      
 