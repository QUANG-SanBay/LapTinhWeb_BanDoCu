from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.models import Buyer
from seller.models import Product

# Create your views here.
def get_home(request):
    return render(request, 'home/home.html')

def get_thongTinDonHang(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'home/xemThongTinSP.html', {'product': product})

@login_required
def get_DatHang(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        try:
            so_luong = int(request.POST.get('so_luong', 1))
            ho_ten = request.POST.get('name')
            so_dien_thoai = request.POST.get('phone')
            dia_chi_giao_hang = request.POST.get('address')
            
            # Lấy buyer từ user hiện tại
            try:
                buyer = Buyer.objects.get(user=request.user)
            except Buyer.DoesNotExist:
                messages.error(request, 'Bạn cần đăng nhập với tài khoản người mua.')
                return redirect('home')
            
            # Gọi phương thức đặt hàng
            result = buyer.dat_hang(
                product_id=product_id,
                so_luong=so_luong,
                dia_chi_giao_hang=dia_chi_giao_hang,
                ho_ten=ho_ten,
                so_dien_thoai=so_dien_thoai
            )
            
            if result['success']:
                messages.success(request, result['message'])
                return redirect('lichSuDonHang')
            else:
                messages.error(request, result['message'])
                return render(request, 'home/datHang.html', {
                    'product': product,
                    'so_luong': so_luong,
                    'ho_ten': ho_ten,
                    'so_dien_thoai': so_dien_thoai,
                    'dia_chi_giao_hang': dia_chi_giao_hang
                })
                
        except ValueError:
            messages.error(request, 'Số lượng không hợp lệ.')
        except Exception as e:
            messages.error(request, f'Có lỗi xảy ra: {str(e)}')
    
    return render(request, 'home/datHang.html', {'product': product})

def get_search(request):
    return render(request, 'home/search.html')

@login_required
def get_lichSuDonHang(request):
    try:
        buyer = Buyer.objects.get(user=request.user)
        orders = buyer.orders.all().order_by('-NgayDatHang')
        return render(request, 'home/lichsudonhang.html', {'orders': orders})
    except Buyer.DoesNotExist:
        messages.error(request, 'Bạn cần đăng nhập với tài khoản người mua.')
        return redirect('home')

def get_profile(request):
    return render(request, 'home/profile.html')

def get_category(request):
    return render(request, 'home/category.html')