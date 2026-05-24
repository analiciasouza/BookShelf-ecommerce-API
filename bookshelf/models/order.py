from django.db import models
from .user import User
from .book import Book
from .payment import PaymentMethod


class Status(models.TextChoices):
        PENDING    = 'pending',    'Aguardando pagamento'
        CONFIRMED  = 'confirmed',  'Confirmado'
        DELIVERING = 'delivering', 'Em entrega'
        DELIVERED  = 'delivered',  'Entregue'
        CANCELLED  = 'cancelled',  'Cancelado'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_number  = models.CharField(max_length=20, unique=True)  # gerado automaticamente
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    total  = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.JSONField()  
    payment_method = models.ForeignKey(PaymentMethod, null=True, on_delete=models.SET_NULL)
    gateway_payment_id = models.CharField(max_length=255, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.order_number:
            from django.utils import timezone
            import random
            self.order_number = f"ORD-{timezone.now().strftime('%Y%m%d')}-{random.randint(1000,9999)}"
        super().save(*args, **kwargs)
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book  = models.ForeignKey(Book, on_delete=models.PROTECT)  # PROTECT: não deixa deletar livro com pedido
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)  # preço na hora da compra


class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses',
    )
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    is_default = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.street_address}, {self.city} - {self.state}"
