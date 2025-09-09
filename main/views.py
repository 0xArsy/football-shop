from django.shortcuts import render
from .models import Product

def show_main(request):
    if Product.objects.count() == 0:
        Product.objects.create(
            name="Bola Adidas Al Rihla",
            price=500000,
            description="Bola resmi Piala Dunia FIFA 2022, dirancang dengan presisi tinggi dan material berkualitas premium untuk performa maksimal di lapangan.",
            thumbnail="https://images.tokopedia.net/img/cache/500-square/VqbcmM/2024/2/15/779aa8d5-2c6b-436d-be61-dea88404c943.png",
            category="Bola",
            is_featured=True,
            quantity=10,
            brand="Adidas"
        )
        Product.objects.create(
            name="Bola Nike Flight",
            price=450000,
            description="Bola latihan dengan teknologi AerowSculpt, memberikan stabilitas udara yang lebih baik dan kontrol optimal bagi pemain.",
            thumbnail="https://down-id.img.susercontent.com/file/id-11134207-7r98s-lztyd93khu3x25",
            category="Bola",
            is_featured=False,
            quantity=4,
            brand="Nike"
        )
        Product.objects.create(
            name="Bola Molten F5A",
            price=300000,
            description="Bola standar resmi FIFA, cocok digunakan dalam kompetisi lokal maupun latihan intensif, dengan daya tahan tinggi.",
            thumbnail="https://alatolahraga.id/wp-content/uploads/2024/12/bola-Molten-5-F5A-1510-CB-1.webp",
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
