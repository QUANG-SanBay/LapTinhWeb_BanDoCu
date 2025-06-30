from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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
    sort = request.GET.get('sort', '')
    products = Product.objects.all()
    if query:
        products = products.filter(TenSanPham__icontains=query)
    # Sắp xếp theo sort
    if sort == 'newest':
        products = products.order_by('-id')
    elif sort == 'bestseller':
        products = products.order_by('-SoLuong')  # hoặc trường bán chạy thực tế nếu có
    elif sort == 'price_asc':
        products = products.order_by('Gia')
    elif sort == 'price_desc':
        products = products.order_by('-Gia')
    # 'relevant' hoặc mặc định thì không cần order lại
    return render(request, 'home/search.html', {'products': products, 'query': query, 'sort': sort})

@login_required
def get_lichSuDonHang(request):
    try:
        buyer = request.user.buyer  # hoặc buyer = request.user.buyer_profile nếu bạn đặt related_name khác
    except Exception:
        return render(request, 'home/lichsudonhang.html', {'orders': []})

    orders = Order.objects.filter(NguoiMua=buyer).order_by('-NgayDatHang')
    return render(request, 'home/lichsudonhang.html', {'orders': orders})
@login_required
def get_profile(request):
    user = request.user
    if request.method == "POST":
        full_name = request.POST.get('name', '').strip()
        # Tách họ tên: last_name là phần đầu, first_name là phần cuối
        if ' ' in full_name:
            parts = full_name.split()
            user.first_name = parts[-1]
            user.last_name = ' '.join(parts[:-1])
        else:
            user.first_name = full_name
            user.last_name = ''
        user.gioi_tinh = request.POST.get('gioi_tinh', user.gioi_tinh)
        user.email = request.POST.get('email', user.email)
        user.so_dien_thoai = request.POST.get('phone', user.so_dien_thoai)
        user.dia_chi = request.POST.get('address', user.dia_chi)
        user.save()
        messages.success(request, "Cập nhật thông tin thành công!")
    return render(request, 'home/profile.html', {'user': user})
def get_category(request, category_id=None):
    categories = ProductCategory.objects.all()
    selected_category = None
    query = request.GET.get('q', '')
    sort = request.GET.get('sort', '')
    products = Product.objects.all()
    if category_id:
        selected_category = ProductCategory.objects.get(id=category_id)
        products = products.filter(DanhMuc_id=category_id)
    if query:
        products = products.filter(TenSanPham__icontains=query)
    # Sắp xếp theo sort
    if sort == 'newest':
        products = products.order_by('-id')
    elif sort == 'bestseller':
        products = products.order_by('-SoLuong')  # hoặc trường bán chạy thực tế nếu có
    elif sort == 'price_asc':
        products = products.order_by('Gia')
    elif sort == 'price_desc':
        products = products.order_by('-Gia')
    return render(request, 'home/category.html', {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
        'query': query,
        'sort': sort,
    })
def all_products(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    return render(request, 'home/all_products.html', {'products': products, 'categories': categories})

def new_products(request):
    products = Product.objects.order_by('-id')
    categories = ProductCategory.objects.all()
    return render(request, 'home/new_products.html', {'products': products, 'categories': categories})
@login_required
def confirm_seller_info(request):
    if request.method == 'POST':
        # Lưu thông tin tạm vào session
        request.session['seller_info'] = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'address': request.POST['address'],
            'cccd': request.POST['cccd'],
        }
        # Sinh OTP và lưu vào session
        otp = str(random.randint(100000, 999999))
        request.session['otp'] = otp
        # Gửi OTP (ở đây chỉ in ra console, thực tế dùng SMS API)
        print(f"OTP gửi đến {request.POST['phone']}: {otp}")
        return redirect('verify_otp')
    return render(request, 'home/confirm_seller_info.html')
@login_required
def verify_otp(request):
    otp = request.session.get('otp')
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        if user_otp == otp:
            # Cập nhật thông tin user
            info = request.session.get('seller_info', {})
            user = request.user
            full_name = info.get('full_name', '').strip()
            # Tách họ tên: last_name là từ đầu tiên, first_name là phần còn lại
            if ' ' in full_name:
                parts = full_name.split()
                user.first_name = parts[-1]  # Tên
                user.last_name = ' '.join(parts[:-1])  # Họ và tên đệm
            else:
                user.first_name = full_name
                user.last_name = ''
            user.email = info.get('email', '')
            user.so_dien_thoai = info.get('phone', '')
            user.dia_chi = info.get('address', '')
            user.cccd = info.get('cccd', '')
            user.user_type = 'seller'
            user.save()
            # Xóa session tạm
            request.session.pop('otp', None)
            request.session.pop('seller_info', None)
            messages.success(request, "Xác thực thành công! Bạn đã trở thành người bán.")
            return redirect('seller:home_seller')
        else:
            messages.error(request, "Mã OTP không đúng. Vui lòng thử lại.")
    return render(request, 'home/verify_otp.html', {'otp': otp})
def terms(request):
    return render(request, 'home/terms.html')