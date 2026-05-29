from bookshelf.models.book import Book
from bookshelf.serializers.book import BookSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class BookView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            try:
                book = Book.objects.get(pk=pk)
                serializer = BookSerializer(book)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Book.DoesNotExist:
                return Response(
                    {'error': 'Livro não encontrado.'}, 
                    status=status.HTTP_404_NOT_FOUND
                )

        books = Book.objects.all() 
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    

class BookDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Book.DoesNotExist:
            return Response({"error" : "Item not found"}, status=status.HTTP_400_BAD_REQUEST)