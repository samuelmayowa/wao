from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('hire/', views.hire, name='hire'),
    path('apply/', views.apply, name='apply'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('terms/', views.terms, name='terms'),
    path('safety/', views.safety, name='safety'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
    path('<slug:category_slug>/', views.category, name='category'),

    ]
