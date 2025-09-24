from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def show_main(request):
    server_user, _ = User.objects.get_or_create(username="Server")
    if Product.objects.count() == 0:
        Product.objects.create(
            name="Bola Adidas Al Rihla",
            price=500000,
            description="Bola resmi Piala Dunia FIFA 2022, dirancang dengan presisi tinggi dan material berkualitas premium untuk performa maksimal di lapangan.",
            thumbnail="https://images.tokopedia.net/img/cache/500-square/VqbcmM/2024/2/15/779aa8d5-2c6b-436d-be61-dea88404c943.png",
            category="Bola",
            is_featured=True,
            quantity=10,
            brand="Adidas",
            user=server_user
        )
        Product.objects.create(
            name="Bola Nike Flight",
            price=450000,
            description="Bola latihan dengan teknologi AerowSculpt, memberikan stabilitas udara yang lebih baik dan kontrol optimal bagi pemain.",
            thumbnail="https://down-id.img.susercontent.com/file/id-11134207-7r98s-lztyd93khu3x25",
            category="Bola",
            is_featured=False,
            quantity=4,
            brand="Nike",
            user=server_user
        )
        Product.objects.create(
            name="Bola Molten F5A",
            price=300000,
            description="Bola standar resmi FIFA, cocok digunakan dalam kompetisi lokal maupun latihan intensif, dengan daya tahan tinggi.",
            thumbnail="https://alatolahraga.id/wp-content/uploads/2024/12/bola-Molten-5-F5A-1510-CB-1.webp",
            category="Bola",
            is_featured=False,
            quantity=15,
            brand="Molten",
            user=server_user
        )

    products = Product.objects.all()
    context = {
        'npm': '2406495836',
        'name': 'Z Arsy Alam Sin',
        'class': 'A',
        'products': products,
        'username': request.user.username if request.user.is_authenticated else None,
        'last_login': request.COOKIES.get('last_login'),
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect("main:show_main")
    return render(request, "create_product.html", {"form": form})

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})

def show_xml(request):
    data = serializers.serialize("xml", Product.objects.all())
    return HttpResponse(data, content_type="application/xml")

def show_json(request):
    data = serializers.serialize("json", Product.objects.all())
    return HttpResponse(data, content_type="application/json")

def show_xml_by_id(request, product_id):
    data = serializers.serialize("xml", Product.objects.filter(pk=product_id))
    return HttpResponse(data, content_type="application/xml")

def show_json_by_id(request, product_id):
    data = serializers.serialize("json", Product.objects.filter(pk=product_id))
    return HttpResponse(data, content_type="application/json")
