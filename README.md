# LapTinhWeb_BanDoCu
Phần mềm bán đồ cũ

### tạo môi trường ảo
```bash
python -m venv venv
```

### kích hoạt môi trường ảo
```bash
.\venv/Scripts/activate
```

### cài đặt Django và Pillow
```bash
pip install django==5.1.3
pip install pillow
```

### thực hiện các lệnh migrate và tạo superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### chạy server
```bash
python manage.py runserver
```
