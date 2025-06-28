from django.contrib import admin
from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('', views.home_seller, name='home_seller'),
    path('dang-ban/', views.dang_ban, name='dang_ban'),
    path('quan-ly-don-hang/', views.quan_ly_don_hang, name='quan_ly_don_hang'),
    path('thong-ke/', views.thong_ke, name='thong_ke'),
    path('them-san-pham/', views.them_san_pham, name='them_san_pham'),
    path('sua-san-pham/<int:id>/', views.sua_san_pham, name='sua_san_pham'),
    path('xoa-san-pham/<int:id>/', views.xoa_san_pham, name='xoa_san_pham'),
    path('danh-sach-san-pham/', views.danh_sach_san_pham, name='danh_sach_san_pham'),
    path('xoa-nhieu-san-pham/', views.xoa_nhieu_san_pham, name='xoa_nhieu_san_pham'),
    path('xem-san-pham/<int:id>/', views.xem_san_pham, name='xem_san_pham'),
    path('cho-xac-nhan/', views.cho_xac_nhan, name='cho_xac_nhan'),
    path('product-detail/', views.get_product_detail, name='get_product_detail'),
]