from bookshelf.models.book import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
   class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'description',
            'genre', 'pages', 'price', 'stock_quantity',
            'status', 'cover_image', 'rating',
            'created_at', 'updated_at',
        ]
