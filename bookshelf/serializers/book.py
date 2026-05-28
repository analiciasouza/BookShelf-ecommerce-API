from bookshelf.models.book import Book
from rest_framework import serializers


class BookSerializier(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields= '__all__'
    
