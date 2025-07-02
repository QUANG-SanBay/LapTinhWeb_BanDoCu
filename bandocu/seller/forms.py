from django import forms
from .models import Product, ProductCategory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['TenSanPham', 'MoTa', 'Gia', 'SoLuong', 'DanhMuc', 'TrangThai', 'HinhAnh', 'HinhAnh2', 'HinhAnh3', 'HinhAnh4']
        widgets = {
            'MoTa': forms.Textarea(attrs={'rows': 4}),
        }