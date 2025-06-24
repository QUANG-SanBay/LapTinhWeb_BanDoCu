from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import User, Buyer, Seller, Admin

# Create your views here.
def get_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, 'Vui lòng nhập đầy đủ thông tin.')
            return render(request, 'account/login.html')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Chào mừng {user.username}!')
            
            # Redirect based on user type
            if user.user_type == 'seller':
                return redirect('seller_home')  # You'll need to create this URL
            elif user.user_type == 'admin':
                return redirect('admin_home')   # You'll need to create this URL
            else:
                return redirect('home')
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng.')
    
    return render(request, 'account/login.html')

def get_register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        full_name = request.POST.get('full_name')
        user_type = request.POST.get('user_type', 'buyer')
        
        # Validation
        errors = []
        
        if not all([username, email, password, password_confirm, full_name]):
            errors.append('Vui lòng điền đầy đủ thông tin.')
        
        if password != password_confirm:
            errors.append('Mật khẩu xác nhận không khớp.')
        
        if len(password) < 6:
            errors.append('Mật khẩu phải có ít nhất 6 ký tự.')
        
        if User.objects.filter(username=username).exists():
            errors.append('Tên đăng nhập đã tồn tại.')
        
        if User.objects.filter(email=email).exists():
            errors.append('Email đã được sử dụng.')
        
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'account/register.html', {
                'username': username,
                'email': email,
                'full_name': full_name,
                'user_type': user_type
            })
        
        try:
            with transaction.atomic():
                # Create user
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=full_name.split()[0] if full_name else '',
                    last_name=' '.join(full_name.split()[1:]) if len(full_name.split()) > 1 else '',
                    user_type=user_type
                )
                
                # Create profile based on user type
                if user_type == 'buyer':
                    Buyer.objects.create(user=user)
                elif user_type == 'seller':
                    Seller.objects.create(user=user)
                elif user_type == 'admin':
                    Admin.objects.create(user=user)
                
                messages.success(request, 'Đăng ký thành công! Vui lòng đăng nhập.')
                return redirect('login')
                
        except Exception as e:
            messages.error(request, f'Có lỗi xảy ra: {str(e)}')
    
    return render(request, 'account/register.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Đăng xuất thành công!')
    return redirect('login')