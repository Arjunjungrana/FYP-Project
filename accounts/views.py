from django.shortcuts import render
from accounts.models import User, UserProfile
from .forms import UserForm,UserProfileForm 
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def reg(request):
    return render(request,'user_auth_page/registration.html')

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'user_auth_page/login.html')


def detectUser(user):
  if user.role == 1:
    redirectUrl = 'workerDashboard'
    return redirectUrl
  elif user.role == 2:
    redirectUrl = 'customerDashboard'
    return redirectUrl
  elif user.role == None and user.is_superadmin:
    redirectUrl = '/admin'
    return redirectUrl

@login_required(login_url='login')
def myAccount(request):
  user = request.user
  redirectUrl = detectUser(user)
  return redirect(redirectUrl)

def check_role_worker(user):
  if user.role == 1:
    return True
  else:
    raise PermissionDenied


def check_role_customer(user):
  if user.role == 2:
    return True
  else:
    raise PermissionDenied


@login_required(login_url='login')
@user_passes_test(check_role_customer)
def customerDashboard(request):    
    return render(request, 'accounts/customerDashboard.html')

@login_required(login_url='login')
@user_passes_test(check_role_worker)
def workerDashboard(request):    
    return render(request, 'accounts/workerDashboard.html')



def registerCustomer(request):
  if request.user.is_authenticated:
    messages.warning(request, 'You are already logged in!')
    return redirect('myAccount')
  elif request.method == 'POST':  
    form = UserForm(request.POST, request.FILES)
    if form.is_valid():
      first_name = form.cleaned_data["first_name"]
      last_name = form.cleaned_data["last_name"]
      username = form.cleaned_data["username"]
      email = form.cleaned_data["email"]
      profile_picture = form.cleaned_data['profile_picture']
      phone_number = form.cleaned_data['phone_number']
      password = form.cleaned_data["password"]
      user = User.objects.create_user(first_name=first_name,last_name=last_name, profile_picture=profile_picture, 
                                      email=email, phone_number=phone_number, username=username, password=password)
      user.role = User.CUSTOMER
      user.save()

      messages.success(request, 'Your account has been registered successfully')
      return redirect('login')
    else:
      print('invalid form')
      print(form.errors)
  else:
    form = UserForm()
    
  context = {
    'form': form,
  }
  return render(request, 'user_auth_page/registration.html', context)




