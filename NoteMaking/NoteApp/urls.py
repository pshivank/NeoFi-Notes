from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.signupPage,name='signuppage'),
    path('signupview',views.signupPage ,name='signupview'),
    path('loginpage',views.loginPage,name='loginpage'),
    path('notes',views.notePage , name='notes'),
    path('logout',views.Logout,name='logout'),
    path('create' , views.noteCreationPage,name='create'),
    path('getnote',views.getnotePage , name='getnote'),
    path('update',views.updatePage , name='update'),
    path('update_note/<int:note_id>/', views.update_note_view, name='update_note'),

]