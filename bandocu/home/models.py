from django.db import models
from account.models import Buyer, Seller
from seller.models import Product

# Create your models here.

class Order(models.Model):
    TRANG_THAI_CHOICES = [
        ('Đang chờ xác nhận', 'Đang chờ xác nhận'),
        ('Đang chuẩn bị hàng', 'Đang chuẩn bị hàng'),
        ('Đang vận chuyển', 'Đang vận chuyển'),
        ('Đã giao hàng', 'Giao hàng thành công'),
        # Có thể thêm các trạng thái khác nếu cần
    ]
    reviewed = models.BooleanField(default=False)
    NguoiMua = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='orders')
    NgayDatHang = models.DateField(auto_now_add=True)
    TongTien = models.DecimalField(max_digits=10, decimal_places=2)
    TrangThaiDonHang = models.CharField(max_length=50, choices=TRANG_THAI_CHOICES, default='Đang chờ xác nhận')
    DiaChiGiaoHang = models.TextField()

    def TaoDonHang(self):
        pass

    def CapNhatTrangThai(self):
        pass

    def HuyDonHang(self):
        pass

    def __str__(self):
        return f"Order {self.id} by {self.NguoiMua.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    SoLuong = models.IntegerField()
    DonGia = models.DecimalField(max_digits=10, decimal_places=2)
    ThanhTien = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def TinhThanhTien(self):
        return self.SoLuong * self.DonGia

    def save(self, *args, **kwargs):
        self.ThanhTien = self.TinhThanhTien()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Item {self.id} of Order {self.order.id}"

class Review(models.Model):
    NguoiMua = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='reviews')
    NguoiBan = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='received_reviews')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    NoiDungDanhGia = models.TextField()
    SoSao = models.IntegerField()
    NgayDanhGia = models.DateField(auto_now_add=True)

    def TaoDanhGia(self):
        pass

    def SuaDanhGia(self):
        pass

    def XoaDanhGia(self):
        self.delete()

    def __str__(self):
        return f"Review {self.id} by {self.NguoiMua.user.username}"
    
class ReviewComment(models.Model):
    review = models.OneToOneField(Review, on_delete=models.CASCADE, related_name='seller_comment')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bình luận của {self.seller.user.username} cho đánh giá {self.review.id}"
