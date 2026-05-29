from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

from bookshelf.ultils import IsOwner

from bookshelf.models.order import Order, OrderItem, Address
from bookshelf.models.book import Book
from bookshelf.serializers.order import (
    OrderSerializer, CreateOrderSerializer, AddressSerializer
)


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class   = OrderSerializer
    http_method_names  = ['get', 'post']  
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related('items__book')

    def create(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data

        with transaction.atomic():
            order = Order.objects.create(
                user             = request.user,
                total            = 0, 
                shipping_address = data['shipping_address'],
                payment_method_id = data['payment_method'],
            )

            total = 0
            for item_data in data['items']:
                book = Book.objects.get(id=item_data['book'])
                OrderItem.objects.create(
                    order      = order,
                    book       = book,
                    quantity   = item_data['quantity'],
                    unit_price = book.price, 
                )
                total += book.price * item_data['quantity']

       
            order.total = total + 2
            order.status = 'confirmed'
            order.save()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

    
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        order = self.get_object()

        if order.status in ['delivered', 'cancelled']:
            return Response(
                {'error': 'Este pedido não pode ser cancelado.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        order.status = 'cancelled'
        order.save()
        return Response(OrderSerializer(order).data)


class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class   = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)