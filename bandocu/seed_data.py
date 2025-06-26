#!/usr/bin/env python
"""
Script để tạo dữ liệu mẫu cho ứng dụng bán đồ cũ
Chạy: python manage.py shell < seed_data.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bandocu.settings')
django.setup()

from account.models import User, Buyer, Seller
from seller.models import ProductCategory, Product
from django.contrib.auth.hashers import make_password

def create_sample_data():
    print("Bắt đầu tạo dữ liệu mẫu...")
    
    # Tạo danh mục sản phẩm
    categories_data = [
        {'TenDanhMuc': 'Điện thoại', 'MoTa': 'Điện thoại di động các loại'},
        {'TenDanhMuc': 'Laptop', 'MoTa': 'Máy tính xách tay'},
        {'TenDanhMuc': 'Bàn/ghế', 'MoTa': 'Nội thất văn phòng'},
        {'TenDanhMuc': 'Sách vở', 'MoTa': 'Sách giáo khoa, tài liệu'},
        {'TenDanhMuc': 'Tai nghe', 'MoTa': 'Tai nghe, loa các loại'},
        {'TenDanhMuc': 'Loa', 'MoTa': 'Loa bluetooth, loa máy tính'},
    ]
    
    categories = []
    for cat_data in categories_data:
        category, created = ProductCategory.objects.get_or_create(
            TenDanhMuc=cat_data['TenDanhMuc'],
            defaults={'MoTa': cat_data['MoTa']}
        )
        categories.append(category)
        if created:
            print(f"Đã tạo danh mục: {category.TenDanhMuc}")
    
    # Tạo người bán
    seller_user, created = User.objects.get_or_create(
        username='seller1',
        defaults={
            'email': 'seller1@example.com',
            'password': make_password('123456'),
            'first_name': 'Nguyễn',
            'last_name': 'Văn Bán',
            'user_type': 'seller'
        }
    )
    
    if created:
        seller = Seller.objects.create(user=seller_user)
        print(f"Đã tạo người bán: {seller_user.username}")
    else:
        seller = seller_user.seller_profile
    
    # Tạo người mua
    buyer_user, created = User.objects.get_or_create(
        username='buyer1',
        defaults={
            'email': 'buyer1@example.com',
            'password': make_password('123456'),
            'first_name': 'Trần',
            'last_name': 'Thị Mua',
            'user_type': 'buyer'
        }
    )
    
    if created:
        buyer = Buyer.objects.create(user=buyer_user)
        print(f"Đã tạo người mua: {buyer_user.username}")
    
    # Tạo sản phẩm mẫu
    products_data = [
        {
            'TenSanPham': 'iPhone 12 64GB - Cũ Đẹp',
            'MoTa': 'iPhone 12 64GB màu xanh, đã sử dụng 1 năm, còn 95% pin, không trầy xước',
            'Gia': 8000000,
            'SoLuong': 5,
            'TrangThai': 'Còn hàng',
            'DanhMuc': categories[0]  # Điện thoại
        },
        {
            'TenSanPham': 'Samsung Galaxy S21 - Cũ',
            'MoTa': 'Samsung Galaxy S21 128GB, màu đen, đã sử dụng 6 tháng, còn 98% pin',
            'Gia': 7500000,
            'SoLuong': 3,
            'TrangThai': 'Còn hàng',
            'DanhMuc': categories[0]  # Điện thoại
        },
        {
            'TenSanPham': 'Laptop Dell Inspiron 15 - Cũ',
            'MoTa': 'Laptop Dell Inspiron 15, Intel i5, 8GB RAM, 256GB SSD, đã sử dụng 2 năm',
            'Gia': 12000000,
            'SoLuong': 2,
            'TrangThai': 'Còn hàng',
            'DanhMuc': categories[1]  # Laptop
        },
        {
            'TenSanPham': 'Bàn làm việc gỗ sồi',
            'MoTa': 'Bàn làm việc gỗ sồi tự nhiên, kích thước 120x60cm, đã sử dụng 1 năm',
            'Gia': 2500000,
            'SoLuong': 1,
            'TrangThai': 'Còn hàng',
            'DanhMuc': categories[2]  # Bàn/ghế
        },
        {
            'TenSanPham': 'Ghế văn phòng Ergonomic',
            'MoTa': 'Ghế văn phòng cao cấp, có đệm lưng, tay vịn điều chỉnh được',
            'Gia': 1800000,
            'SoLuong': 4,
            'TrangThai': 'Còn hàng',
            'DanhMuc': categories[2]  # Bàn/ghế
        },
        {
            'TenSanPham': 'Sách Toán 12 - Bộ GD&ĐT',
            'MoTa': 'Sách giáo khoa Toán 12, bộ cũ nhưng còn mới, không viết vẽ',
            'Gia': 50000,
            'SoLuong': 10,
            'TrangThai': 'Còn hàng',
            'DanhMuc': categories[3]  # Sách vở
        },
        {
            'TenSanPham': 'Tai nghe Sony WH-1000XM4',
            'MoTa': 'Tai nghe chống ồn Sony, đã sử dụng 1 năm, còn 90% pin',
            'Gia': 3500000,
            'SoLuong': 2,
            'TrangThai': 'Còn hàng',
            'DanhMuc': categories[4]  # Tai nghe
        },
        {
            'TenSanPham': 'Loa JBL Flip 5',
            'MoTa': 'Loa bluetooth JBL Flip 5, màu xanh, đã sử dụng 6 tháng',
            'Gia': 1200000,
            'SoLuong': 3,
            'TrangThai': 'Còn hàng',
            'DanhMuc': categories[5]  # Loa
        },
        {
            'TenSanPham': 'iPhone 13 Pro 128GB',
            'MoTa': 'iPhone 13 Pro 128GB, màu xanh Sierra, đã sử dụng 3 tháng',
            'Gia': 15000000,
            'SoLuong': 1,
            'TrangThai': 'Còn hàng',
            'DanhMuc': categories[0]  # Điện thoại
        },
        {
            'TenSanPham': 'MacBook Air M1 256GB',
            'MoTa': 'MacBook Air M1 256GB, màu bạc, đã sử dụng 1 năm',
            'Gia': 25000000,
            'SoLuong': 1,
            'TrangThai': 'Còn hàng',
            'DanhMuc': categories[1]  # Laptop
        },
        {
            'TenSanPham': 'Bộ sách Văn 12 (3 cuốn)',
            'MoTa': 'Bộ sách giáo khoa Văn 12 gồm 3 cuốn, còn mới 90%',
            'Gia': 80000,
            'SoLuong': 5,
            'TrangThai': 'Còn hàng',
            'DanhMuc': categories[3]  # Sách vở
        },
        {
            'TenSanPham': 'AirPods Pro 2',
            'MoTa': 'AirPods Pro 2, đã sử dụng 4 tháng, còn 95% pin',
            'Gia': 4500000,
            'SoLuong': 2,
            'TrangThai': 'Còn hàng',
            'DanhMuc': categories[4]  # Tai nghe
        }
    ]
    
    for product_data in products_data:
        product, created = Product.objects.get_or_create(
            TenSanPham=product_data['TenSanPham'],
            defaults={
                'MoTa': product_data['MoTa'],
                'Gia': product_data['Gia'],
                'SoLuong': product_data['SoLuong'],
                'TrangThai': product_data['TrangThai'],
                'NguoiBan': seller,
                'DanhMuc': product_data['DanhMuc']
            }
        )
        if created:
            print(f"Đã tạo sản phẩm: {product.TenSanPham}")
    
    print("\n=== THÔNG TIN ĐĂNG NHẬP ===")
    print("Người bán:")
    print("  Username: seller1")
    print("  Password: 123456")
    print("  Email: seller1@example.com")
    print("\nNgười mua:")
    print("  Username: buyer1")
    print("  Password: 123456")
    print("  Email: buyer1@example.com")
    print("\nĐã tạo xong dữ liệu mẫu!")

if __name__ == '__main__':
    create_sample_data() 