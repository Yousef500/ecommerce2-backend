from django.urls import path

from .views import getProducts, getProduct

urlpatterns = [
    path('products/', getProducts, name='product-list'),
    path('products/<str:pk>/', getProduct, name='product-detail'),
]
