from django.db import models
from account.models import Seller as AccountSeller


# Create your models here.
class ProductCategory(models.Model):
    TenDanhMuc = models.CharField(max_length=150)
    MoTa = models.TextField(blank=True, null=True)

    def ThemDanhMuc(self):
        pass

    def SuaDanhMuc(self):
        pass

    def XoaDanhMuc(self):
        pass

    def __str__(self):
        return self.TenDanhMuc

class Product(models.Model):
    TenSanPham = models.CharField(max_length=255)
    MoTa = models.TextField(blank=True, null=True)
    Gia = models.DecimalField(max_digits=10, decimal_places=2)
    SoLuong = models.IntegerField()
    TrangThai = models.CharField(max_length=50)
    NgayDang = models.DateField(auto_now_add=True)
    NguoiBan = models.ForeignKey(AccountSeller, on_delete=models.CASCADE, related_name='products')
    DanhMuc = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    HinhAnh = models.ImageField(upload_to='products/', blank=True, null=True)

    def XemChiTiet(self):
        return self

    def CapNhatThongTin(self):
        pass

    def Xoa(self):
        self.delete()

    def __str__(self):
        return self.TenSanPham
