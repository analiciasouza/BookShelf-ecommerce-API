from rest_framework import serializers
from bookshelf.models.payment import PaymentMethod, Payment



class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'user', 'type', 'card_brand', 'last_four_digits'
                  'holder_name', 'is_default']
        

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'