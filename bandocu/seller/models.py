from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TheLoai(models.Model):
    tenTheLoai = models.CharField(max_length=255)

    def __str__(self):
        return self.tenTheLoai

class SanPham(models.Model):
    nguoiBan = models.ForeignKey(User, on_delete=models.CASCADE)
    tenSanPham = models.CharField(max_length=255)
    moTa = models.TextField()
    gia = models.DecimalField(max_digits=10, decimal_places=2)
    soLuong = models.IntegerField()
    theLoai = models.ForeignKey(TheLoai, on_delete=models.SET_NULL, null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    ngayTao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tenSanPham

class AnhSanPham(models.Model):
    sanPham = models.ForeignKey(SanPham, related_name='hinhAnh', on_delete=models.CASCADE)
    hinhAnh = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.sanPham.tenSanPham}"
