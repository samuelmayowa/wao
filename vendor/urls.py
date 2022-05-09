from django.contrib.auth import views as auth_views

from django.urls import path

from . import views

urlpatterns = [
    path('become_vendor/', views.become_vendor, name='become_vendor'),
    path('vendor_admin/', views.vendor_admin, name='vendor_admin'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_vendor/', views.edit_vendor, name='edit_vendor'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('add_images/', views.addimages, name='add_images'),


    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),

]