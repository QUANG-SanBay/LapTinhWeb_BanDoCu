from django.shortcuts import render

# Create your views here.
def get_homeSeller(request):
    return render(request, 'seller/home-seller.html')

def get_dangBan(request):
    return render(request, 'seller/dang-ban.html')

def get_quanLyDonHang(request):
    return render(request, 'seller/quan-ly-don-hang.html')

def get_thongKe(request):
    return render(request, 'seller/thong-ke.html')