from django.shortcuts import render
from .models import Product

def show_main(request):
    # Jika database masih kosong, tambahkan 3 produk bola
    if Product.objects.count() == 0:
        Product.objects.create(
            name="Bola Adidas Al Rihla",
            price=500000,
            description="Bola resmi Piala Dunia FIFA 2022, kualitas premium.",
            thumbnail="https://assets.adidas.com/images/w_600,f_auto,q_auto/bola_adidas.jpg",
            category="Bola",
            is_featured=True,
            quantity=10,
            brand="Adidas"
        )
        Product.objects.create(
            name="Bola Nike Flight",
            price=450000,
            description="Bola latihan dengan teknologi AerowSculpt untuk stabilitas.",
            thumbnail="https://static.nike.com/bola_nike.jpg",
            category="Bola",
            is_featured=False,
            quantity=8,
            brand="Nike"
        )
        Product.objects.create(
            name="Bola Molten F5A",
            price=300000,
            description="Bola standar FIFA cocok untuk kompetisi lokal.",
            thumbnail="https://molten.com/bola_molten.jpg",
            category="Bola",
            is_featured=False,
            quantity=15,
            brand="Molten"
        )

    products = Product.objects.all()
    context = {
        'name': 'Z Arsy Alam Sin',
        'class': 'A',
        'products': products
    }
    return render(request, "main.html", context)
