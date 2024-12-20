
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views



urlpatterns = [
    path('',views.reg,name='reg'),
    path('login',views.login,name='login'),
    path('myAccount/', views.myAccount, name="myAccount"),
    path('customerDashboard/', views.customerDashboard, name="customerDashboard"),
    path('registercustomer/',views.registerCustomer,name='registercustomer')

 

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

