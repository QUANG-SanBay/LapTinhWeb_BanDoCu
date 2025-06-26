from django.contrib import admin
from .models import Buyer, Seller, Admin, User

# Register your models here.
admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Admin)
admin.site.register(User)
