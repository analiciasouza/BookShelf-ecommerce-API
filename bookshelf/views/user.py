from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from bookshelf.ultils import IsOwner
from bookshelf.models.user import User
from bookshelf.serializers.user import UserSerializer, RegisterSerializer

class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.save()
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'user': UserSerializer(user).data,
            'tokens': {
                'access':  str(refresh.access_token),
                'refresh': str(refresh),
            }
        }, status=status.HTTP_201_CREATED)
        

class LoginUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email    = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {'error': 'Email e senha são obrigatórios.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        
        from django.contrib.auth import authenticate
        user = authenticate(request, email=email, password=password)

        if not user:
            return Response(
                {'error': 'Credenciais inválidas.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            'user': UserSerializer(user).data,
            'tokens': {
                'access':  str(refresh.access_token),
                'refresh': str(refresh),
            }
        })
    
class UserView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]  

    def get(self, request):
        return Response(UserSerializer(request.user).data)