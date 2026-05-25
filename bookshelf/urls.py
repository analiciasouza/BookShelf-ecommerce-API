from django.urls import include, path
from rest_framework.routers import DefaultRouter

from bookshelf.views.book import BookViewSet
from bookshelf.views.user import UserViewSet
from bookshelf.views.order import AddressViewSet, OrderItemViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'order-items', OrderItemViewSet, basename='order-item')
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]
