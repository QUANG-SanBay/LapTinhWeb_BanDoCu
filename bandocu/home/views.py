from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from seller.models import Product,  ProductCategory
from .models import Order
# Create your views here.
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
    is_buyer = False
    if request.user.is_authenticated:
        is_buyer = hasattr(request.user, 'buyer')  # hoặc 'buyer_profile' nếu bạn đặt related_name
    return render(request, 'home/xemThongTinSP.html', {'product': product, 'is_buyer': is_buyer})

@login_required
def get_DatHang(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        # Lấy thông tin từ form
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        so_luong = int(request.POST.get('so_luong', 1))

        # Lấy buyer từ user hiện tại
        buyer = request.user.buyer

        # Tạo đơn hàng mới
        from .models import Order, OrderItem
        order = Order.objects.create(
            NguoiMua=buyer,
            DiaChiGiaoHang=address,
            TongTien=product.Gia * so_luong,
            TrangThaiDonHang="Chờ xác nhận"
        )
        # Thêm sản phẩm vào OrderItem
        OrderItem.objects.create(
            order=order,
            product=product,
            SoLuong=so_luong,
            DonGia=product.Gia
        )
        # Trừ số lượng tồn kho
        product.SoLuong -= so_luong
        product.save()
        return render(request, 'home/datHang.html', {'success': True, 'product': product})

    return render(request, 'home/datHang.html', {'product': product})

def get_search(request):
    query = request.GET.get('q', '')
    products = Product.objects.all()
    if query:
        products = products.filter(TenSanPham__icontains=query)
    return render(request, 'home/search.html', {'products': products, 'query': query})

@login_required
def get_lichSuDonHang(request):
    try:
        buyer = request.user.buyer  # hoặc buyer = request.user.buyer_profile nếu bạn đặt related_name khác
    except Exception:
        return render(request, 'home/lichsudonhang.html', {'orders': []})

    orders = Order.objects.filter(NguoiMua=buyer).order_by('-NgayDatHang')
    return render(request, 'home/lichsudonhang.html', {'orders': orders})
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
def get_confirm_seller_info(request):
    if request.method == 'POST':
        # Xử lý thông tin xác nhận người bán
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        # Lưu thông tin vào cơ sở dữ liệu hoặc xử lý theo yêu cầu
        return render(request, 'home/confirm_seller_info.html', {'success': True})

    return render(request, 'home/confirm_seller_info.html', {'success': False})
def terms(request):
    return render(request, 'home/terms.html')