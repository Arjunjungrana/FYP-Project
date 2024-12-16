from django.shortcuts import render


# Create your views here.
def reg(request):
    return render(request,'user_auth_page/registration.html')

def home(request):
    return render(request,'home.html')