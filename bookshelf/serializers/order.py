from rest_framework import serializers
from bookshelf.models.order import Order, OrderItem, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Address
        fields = [
            'id', 'street_address', 'city',
            'state', 'postal_code', 'country', 'is_default'
        ]
       

class OrderItemSerializer(serializers.ModelSerializer):
    book_title  = serializers.CharField(source='book.title', read_only=True)
    book_cover  = serializers.ImageField(source='book.cover_image', read_only=True)

    class Meta:
        model  = OrderItem
        fields = ['id', 'book', 'book_title', 'book_cover', 'quantity', 'unit_price']


class OrderSerializer(serializers.ModelSerializer):
    items  = OrderItemSerializer(many=True, read_only=True)  
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model  = Order
        fields = [
            'id', 'order_number', 'status', 'status_display',
            'total', 'shipping_fee', 'shipping_address',
            'payment_method', 'items', 'created_at'
        ]
        read_only_fields = ['order_number', 'created_at']


class CreateOrderSerializer(serializers.Serializer):
    items = serializers.ListField(child=serializers.DictField())
    shipping_address = serializers.DictField()
    payment_method   = serializers.IntegerField()

    def validate_items(self, items):
        if not items:
            raise serializers.ValidationError('O pedido precisa ter pelo menos 1 item.')
        return items