from django.shortcuts import render, get_object_or_404
from seller.models import Product
# Create your views here.
from seller.models import Product, ProductCategory
import random

def get_home(request):
    # Gợi ý sản phẩm: 12 sản phẩm ngẫu nhiên
    all_products = list(Product.objects.all())
    random.shuffle(all_products)
    suggested_products = all_products[:12]

    # Sản phẩm mới: 12 sản phẩm mới nhất
    new_products = Product.objects.order_by('-id')[:12]

    categories = ProductCategory.objects.all()
    return render(request, 'home/home.html', {
        'products': suggested_products,
        'new_products': new_products,
        'categories': categories
    })
    return render(request, 'home/home.html', {'products': products, 'categories': categories})

def get_thongTinDonHang(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'home/xemThongTinSP.html', {'product': product})

def get_DatHang(request):
    return render(request, 'home/datHang.html')

def get_search(request):
    query = request.GET.get('q', '')
    products = Product.objects.all()
    if query:
        products = products.filter(TenSanPham__icontains=query)
    return render(request, 'home/search.html', {'products': products, 'query': query})

def get_lichSuDonHang(request):
    return render(request, 'home/lichsudonhang.html')
def get_profile(request):
    user = request.user
    return render(request, 'home/profile.html', {'user': user})
def get_category(request, category_id=None):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    selected_category = None
    if category_id:
        selected_category = ProductCategory.objects.get(id=category_id)
        products = products.filter(DanhMuc_id=category_id)
    return render(request, 'home/category.html', {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
    })
def all_products(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    return render(request, 'home/all_products.html', {'products': products, 'categories': categories})

def new_products(request):
    products = Product.objects.order_by('-id')
    categories = ProductCategory.objects.all()
    return render(request, 'home/new_products.html', {'products': products, 'categories': categories})