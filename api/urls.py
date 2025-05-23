from django.urls import path
from .views import ProductView, OrderView, OrderDetailView

urlpatterns = [
    path('products/', ProductView.as_view(), name='product-list'),
    path('orders/', OrderView.as_view(), name='order-list'),
    path('order-details/', OrderDetailView.as_view(), name='order-detail-list'),
]
