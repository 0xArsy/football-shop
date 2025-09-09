from django.shortcuts import render
from .models import Product

def show_main(request):
    products = Product.objects.all()  # ambil semua produk
    context = {
        'app_name': 'Football Shop',
        'student_name': 'Z Arsy Alam Sin',
        'student_class': 'A',
        'products': products,
    }
    return render(request, "main.html", context)
