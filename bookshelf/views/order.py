from models.order import Order, OrderItem, Address 
from serializers.order import OrderSerializer, OrderItemSerializer, AddressSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from bookshelf.ultils import IsOwner

class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = [ IsAuthenticated, IsOwner]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

