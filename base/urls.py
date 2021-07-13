from django.urls import path

from .views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<str:pk>/',
         ProductRetrieveUpdateDestroyAPIView.as_view(),
         name='product-detail'),
]
