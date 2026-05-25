from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from bookshelf.ultils import IsOwner
from models.user import User
from serializers.user import UserSerializer

class UserViewSet(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer