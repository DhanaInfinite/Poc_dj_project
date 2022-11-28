from pocapp.models import Customer,Product,Order
from rest_framework.serializers import ModelSerializer
class CustomerSerializer(ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'