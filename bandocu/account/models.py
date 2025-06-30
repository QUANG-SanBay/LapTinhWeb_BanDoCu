from django.db import models
from django.db import transaction
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.


class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Nam'),
        ('F', 'Nữ'),
        ('O', 'Khác'),
    )
    
    # Override username field to use email
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    gioi_tinh = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    dia_chi = models.TextField(blank=True, null=True)
    so_dien_thoai = models.CharField(max_length=20, blank=True, null=True)
    ngay_dang_ky = models.DateField(auto_now_add=True)
    
    # User type field
    USER_TYPE_CHOICES = (
        ('buyer', 'Người mua'),
        ('seller', 'Người bán'),
        ('admin', 'Quản trị viên'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='buyer')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer_profile')
    
    def TimKiemSanPham(self):
        return []  # return list of Product

    def LocSanPham(self):
        return []

    def LuuSanPhamYeuThich(self, product):
        pass

    def dat_hang(self, product_id, so_luong, dia_chi_giao_hang, ho_ten, so_dien_thoai):
        """
        Phương thức đặt hàng với kiểm tra tồn kho
        """
        # Import here to avoid circular import
        from seller.models import Product
        from home.models import Order, OrderItem
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return {'success': False, 'message': 'Sản phẩm không tồn tại.'}

        # Kiểm tra tồn kho
        if product.SoLuong < so_luong:
            return {'success': False, 'message': 'Đặt hàng thất bại. Sản phẩm hết hàng.'}

        try:
            with transaction.atomic():
                # Trừ tồn kho
                product.SoLuong -= so_luong
                product.save()

                # Tạo đơn hàng
                tong_tien = product.Gia * so_luong
                order = Order.objects.create(
                    NguoiMua=self,
                    TongTien=tong_tien,
                    TrangThaiDonHang='Đã đặt hàng',
                    DiaChiGiaoHang=dia_chi_giao_hang
                )

                # Tạo chi tiết đơn hàng
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    SoLuong=so_luong,
                    DonGia=product.Gia,
                    ThanhTien=tong_tien
                )

            return {
                'success': True, 
                'message': 'Đặt hàng thành công!', 
                'order_id': order.id,
                'tong_tien': tong_tien
            }

        except Exception as e:
            return {'success': False, 'message': f'Đặt hàng thất bại: {str(e)}'}

    def ThanhToan(self, order):
        pass

    def DanhGiaNguoiBan(self, seller, rating, comment):
        pass

    def XemLichSuGiaoDich(self):
        return []

    def HuyDonHang(self, order):
        pass

    def __str__(self):
        return f"Buyer: {self.user.username}"

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller_profile')
    
    def DangBanSanPham(self, product):
        pass

    def SuaSanPham(self, product):
        pass

    def XoaSanPham(self, product):
        pass

    def QuanLySanPham(self):
        return []

    def NhanDonHang(self):
        return []

    def XuLyDonHang(self, order):
        pass

    def CapNhatThongTinDonHang(self, order):
        pass

    def NhanVaTraLoiDanhGia(self):
        return []

    def XemThongKeBanHang(self):
        pass  # Return Report

    def __str__(self):
        return f"Seller: {self.user.username}"

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    
    def QuanLyNguoiDung(self):
        pass

    def QuanLyDanhMucSanPham(self):
        pass

    def DuyetSanPham(self, product):
        pass

    def GiaiQuyetTranhChap(self):
        pass

    def XemBaoCaoThongKe(self):
        pass  # Return Report

    def SaoLuuDuLieu(self):
        pass

    def PhucHoiDuLieu(self):
        pass

    def __str__(self):
        return f"Admin: {self.user.username}"
