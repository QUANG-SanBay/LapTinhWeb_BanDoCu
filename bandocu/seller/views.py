from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .models import Product, ProductCategory
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_seller(request):
    seller = request.user.seller_profile
    products = Product.objects.filter(NguoiBan=seller).select_related('DanhMuc')
    # Lấy danh sách danh mục có sản phẩm của seller
    categories = ProductCategory.objects.filter(products__NguoiBan=seller).distinct()
    # Gom sản phẩm theo danh mục
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
            return redirect('seller:home_seller')
    else:
        form = ProductForm()
    return render(request, 'seller/dang-ban.html', {'form': form})

def quan_ly_don_hang(request):
    return render(request, 'seller/quan-ly-don-hang.html')

def thong_ke(request):
    return render(request, 'seller/thong-ke.html')

def them_san_pham(request):
    return render(request, 'seller/them-san-pham.html')

def sua_san_pham(request, id):
    return render(request, 'seller/sua-san-pham.html')
def xoa_san_pham(request, id):
    return render(request, 'seller/xoa-san-pham.html')

def danh_sach_san_pham(request):
    return render(request, 'seller/danh-sach-san-pham.html')

def xoa_nhieu_san_pham(request):
    return render(request, 'seller/xoa-nhieu-san-pham.html')

def xem_san_pham(request, id):
    # Dữ liệu mẫu cho sản phẩm
    # san_pham = {
    #     'id': id,
    #     'tenSanPham': 'iPhone 11 Pro Max',
    #     'gia': 15500000,
    #     'soLuong': 10,
    #     'moTa': 'iPhone 11 Pro Max là chiếc iPhone cao cấp nhất của Apple với màn hình 6.5 inch, chip A13 Bionic mạnh mẽ, camera 3 ống kính và pin trâu. Sản phẩm được bảo hành chính hãng 12 tháng.',
    #     'ngayTao': '2024-01-15',
    #     'theLoai': {'tenTheLoai': 'Điện thoại'},
    #     'hinhAnh': [{'hinhAnh': {'url': '/static/seller/ip11.jpg'}}]
    # }
    return render(request, 'seller/xem-san-pham.html')
    # return render(request, 'seller/xem-san-pham.html', {'san_pham': san_pham})
def cho_xac_nhan(request):
    return render(request, 'seller/cho-xac-nhan.html')