from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .models import Product, ProductCategory
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from home.models import Review
from django.db import models


# Create your views here.
def home_seller(request):
    user = request.user
    # Kiểm tra user đã có seller_profile chưa
    seller = getattr(user, 'seller_profile', None)
    if not seller:
        messages.error(request, "Tài khoản của bạn chưa đăng ký làm người bán.")
        return redirect('home')  # hoặc trang phù hợp, ví dụ: trang đăng ký seller
    products = Product.objects.filter(NguoiBan=seller).select_related('DanhMuc')
    categories = ProductCategory.objects.filter(products__NguoiBan=seller).distinct()
    products_by_category = {}
    for category in categories:
        products_by_category[category.TenDanhMuc] = products.filter(DanhMuc=category)
    return render(request, 'seller/home-seller.html', {
        'products': products,
        'products_by_category': products_by_category,
        'categories': categories,
    })


@login_required
def dang_ban(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.NguoiBan = request.user.seller_profile
            product.save()
            return redirect('seller:danh_sach_san_pham')  # chuyển về danh sách sản phẩm
    else:
        form = ProductForm()
    return render(request, 'seller/dang-ban.html', {'form': form})

def quan_ly_don_hang(request):
    return render(request, 'seller/quan-ly-don-hang.html')

def thong_ke(request):
    return render(request, 'seller/thong-ke.html')

def them_san_pham(request):
    return render(request, 'seller/them-san-pham.html')

@login_required
def sua_san_pham(request, id):
    product = get_object_or_404(Product, pk=id, NguoiBan=request.user.seller_profile)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('seller:xem_san_pham', id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'seller/sua-san-pham.html', {'form': form, 'san_pham': product})
def xoa_san_pham(request, id):
    return render(request, 'seller/xoa-san-pham.html')

def danh_sach_san_pham(request):
    seller = request.user.seller_profile
    products = Product.objects.filter(NguoiBan=seller).select_related('DanhMuc')
    return render(request, 'seller/danh-sach-san-pham.html', {'products': products})

def xoa_nhieu_san_pham(request):
    return render(request, 'seller/xoa-nhieu-san-pham.html')

@login_required
def xem_san_pham(request, id):
    product = get_object_or_404(Product, pk=id)
    reviews = product.reviews.select_related('NguoiMua__user', 'NguoiBan__user').all()
    seller = getattr(product, 'NguoiBan', None)
    seller_full_name = f"{seller.user.last_name} {seller.user.first_name}" if seller else ""
    avg_star = reviews.aggregate(models.Avg('SoSao'))['SoSao__avg'] or 0
    avg_star = round(avg_star, 1)
    return render(request, 'seller/xem-san-pham.html', {
        'product': product,
        'reviews': reviews,
        'user': request.user,
        'seller_full_name': seller_full_name,
        'avg_star': avg_star,
    })
def cho_xac_nhan(request):
    return render(request, 'seller/cho-xac-nhan.html')
def get_product_detail(request):
    return render(request, 'seller/product-detail.html')
