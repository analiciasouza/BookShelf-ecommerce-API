from models.book import Book
from serializers.book import BookSerialzier
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class BookView(generics.ListAPIView,
                  generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerialzier