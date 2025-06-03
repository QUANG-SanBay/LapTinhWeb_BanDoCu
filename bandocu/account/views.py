from django.shortcuts import render

# Create your views here.
def get_login(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     # Authentication logic here
    #     # For now, just render a template with the username
    #     return render(request, 'account/login_success.html', {'username': username})
    return render(request, 'account/login.html')
def get_register(request):
    return render(request, 'account/register.html')