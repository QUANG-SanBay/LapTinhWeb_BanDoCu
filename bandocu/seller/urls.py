from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     path('',views.get_homeSeller,name='homeSeller'),
     path('dang-ban/', views.get_dangBan, name='dangBan'),
     path('quan-ly-don-hang/', views.get_quanLyDonHang, name='quanLyDonHang'),
     path('thong-ke/', views.get_thongKe, name='thongKe'),
]