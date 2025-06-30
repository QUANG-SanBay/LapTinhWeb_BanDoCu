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
     path('category/', views.get_category, name='category'),
     path('category/<int:category_id>/', views.get_category, name='category_detail'),
     path('all-products/', views.all_products, name='all_products'),
     path('new-products/', views.new_products, name='new_products'),
     path('dathang/<int:product_id>/', views.get_DatHang, name='datHang'),
     path('confirm_seller_info/', views.get_confirm_seller_info, name='confirm_seller_info'),
     path('confirm_seller_info/<int:product_id>/', views.get_confirm_seller_info, name='confirm_seller_info_with_product'),
     path('terms/', views.terms, name='terms'),
]