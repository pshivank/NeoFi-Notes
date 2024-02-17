from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.signupPage,name='signuppage'),
    path('signupview',views.signupPage ,name='signupview'),
    path('loginpage',views.loginPage,name='loginpage'),
    path('notes',views.notePage , name='notes'),
    path('logout',views.Logout,name='logout'),

]