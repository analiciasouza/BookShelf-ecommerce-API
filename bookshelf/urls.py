from django.urls import include, path
from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from bookshelf.views.book import BookView, BookDetailView
from bookshelf.views.order import AddressViewSet, OrderViewSet
from bookshelf.views.payment import PaymentViewSet

from rest_framework_simplejwt.views import TokenRefreshView
from bookshelf.views.user import RegisterUserView, LoginUserView, UserView




router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
router.register(f'payments', PaymentViewSet, basename='payment' )
router.register(r'addresses', AddressViewSet, basename='address')


urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookView.as_view(), name='book-list'),
    path('books/<int:book_id>', BookDetailView.as_view(), name='book-detail'),
    path('auth/register/', RegisterUserView.as_view()),
    path('auth/login/',    LoginUserView.as_view()),
    path('auth/refresh/',  TokenRefreshView.as_view()),  
    path('auth/user/',       UserView.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)