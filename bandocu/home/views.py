from django.shortcuts import render

# Create your views here.
def get_home(request):
    return render(request, 'home/home.html')

def get_thongTinDonHang(request):
    return render(request, 'home/xemThongTinSP.html')

def get_DatHang(request):
    return render(request, 'home/datHang.html')

def get_search(request):
    return render(request, 'home/search.html')

def get_lichSuDonHang(request):
    return render(request, 'home/lichsudonhang.html')