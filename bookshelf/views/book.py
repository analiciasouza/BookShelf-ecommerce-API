from models.book import Book
from serializers.book import BookSerialzier
from rest_framework import viewsets
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerialzier