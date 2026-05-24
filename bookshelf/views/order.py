from models.order import Order, OrderItem, Address 
from serializers.order import OrderSerializer, OrderItemSerializer, AddressSerializer
from rest_framework import viewsets
from rest_framework.response import Response


# TODO fazer classe de permissao de só aparecer o que for do usuário
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

