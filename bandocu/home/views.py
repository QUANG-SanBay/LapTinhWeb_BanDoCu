from django.shortcuts import render, get_object_or_404
from seller.models import Product
# Create your views here.
from seller.models import Product

def get_home(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm
    return render(request, 'home/home.html', {'products': products})

def get_thongTinDonHang(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'home/xemThongTinSP.html', {'product': product})

def get_DatHang(request):
    return render(request, 'home/datHang.html')

def get_search(request):
    return render(request, 'home/search.html')

def get_lichSuDonHang(request):
    return render(request, 'home/lichsudonhang.html')
def get_profile(request):
    return render(request, 'home/profile.html')
def get_category(request):
    return render(request, 'home/category.html')