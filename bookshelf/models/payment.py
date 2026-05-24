from django.db import models
from .user import User


class Type(models.TextChoices):
        CREDIT_CARD = 'credit_card', 'Cartão de Crédito'
        DEBIT_CARD  = 'debit_card',  'Cartão de Débito'
        PIX         = 'pix',         'Pix'

class Status(models.TextChoices):
        PENDING   = 'pending',   'Pendente'
        APPROVED  = 'approved',  'Aprovado'
        REJECTED  = 'rejected',  'Recusado'
        REFUNDED  = 'refunded',  'Estornado'


class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_methods')
    type = models.CharField(max_length=20, choices=Type.choices)
    gateway_token = models.CharField(max_length=255)   
    last_four_digits= models.CharField(max_length=4, blank=True)
    card_brand = models.CharField(max_length=50, blank=True)  
    holder_name = models.CharField(max_length=100, blank=True)
    is_default  = models.BooleanField(default=False)
    

class Payment(models.Model):
    order = models.OneToOneField('Order', on_delete=models.CASCADE, related_name='payment')
    payment_method = models.ForeignKey(PaymentMethod, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    paid_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
