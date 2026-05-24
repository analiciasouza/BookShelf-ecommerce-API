from models.book import Book
from rest_framework import serializers


class BookSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields= '__all__'
    
