from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.loginPage, name='Login_Page'),    
   # path('Reg_Page/', views.registerPage, name='Reg_Page'),
    path('logou_tUser/', views.logoutUser, name='logou_tUser'),
      

]
