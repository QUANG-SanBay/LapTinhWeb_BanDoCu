from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     path('',views.get_home,name='home'),
     path('chiTietSP/<int:product_id>/',views.get_thongTinDonHang,name='chiTietSP'),
     path('chiTietSP/',views.get_thongTinDonHang,name='chiTietSP'),
     path('dathang/<int:product_id>/',views.get_DatHang,name='datHang'),
     path('lichSuDonHang/',views.get_lichSuDonHang,name='lichSuDonHang'),
     path('search/',views.get_search,name='search'),
     path('profile/',views.get_profile,name='profile'),
     path('category/',views.get_category,name='category'),
     path('category/<int:category_id>/',views.get_category,name='category_detail'),
]