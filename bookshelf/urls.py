from django.urls import include, path
from rest_framework.routers import DefaultRouter

from bookshelf.views.book import BookView
from bookshelf.views.order import AddressViewSet, OrderItemViewSet, OrderViewSet

from rest_framework_simplejwt.views import TokenRefreshView
from bookshelf.views.user import RegisterUserView, LoginUserView, UserView




router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'addresses', AddressViewSet, basename='address')


urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookView.as_view()),
    path('auth/register/', RegisterUserView.as_view()),
    path('auth/login/',    LoginUserView.as_view()),
    path('auth/refresh/',  TokenRefreshView.as_view()),  
    path('auth/user/',       UserView.as_view()),
]
