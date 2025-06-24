from django.db import models

# Create your models here.

class User(models.Model):
    TenDangNhap = models.CharField(max_length=150)
    MatKhau = models.CharField(max_length=128)
    Email = models.EmailField(unique=True)
    GioiTinh = models.CharField(max_length=10, blank=True, null=True)
    DiaChi = models.TextField(blank=True, null=True)
    SoDienThoai = models.CharField(max_length=20, blank=True, null=True)
    NgayDangKy = models.DateField(auto_now_add=True)

    def DangKy(self):
        pass  # implement registration logic

    def DangNhap(self):
        pass  # implement login logic

    def DangXuat(self):
        pass  # implement logout logic

    def CapNhatThongTin(self):
        pass  # implement update info logic

class Buyer(User):
    def TimKiemSanPham(self):
        return []  # return list of Product

    def LocSanPham(self):
        return []

    def LuuSanPhamYeuThich(self, product):
        pass

    def DatHang(self, cart):
        pass

    def ThanhToan(self, order):
        pass

    def DanhGiaNguoiBan(self, seller, rating, comment):
        pass

    def XemLichSuGiaoDich(self):
        return []

    def HuyDonHang(self, order):
        pass

class Seller(User):
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

class Admin(User):
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
