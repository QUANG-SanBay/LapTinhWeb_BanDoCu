from django.shortcuts import render

# Create your views here.
def get_homeSeller(request):
    return render(request, 'seller/home-seller.html')