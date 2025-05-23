from .models import Product, Order, OrderDetail
from rest_framework.serializers import ModelSerializer
# from user_auth.user_serializer import UserListingSerializer

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields='__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields='__all__'

class OrderDetailSerializer(ModelSerializer):
    class Meta:
        model = OrderDetail
        fields='__all__'        
