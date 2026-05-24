from django.contrib.auth import get_user_model
from django.test import TestCase

from bookshelf.models import Address


class UserModelTests(TestCase):
    def test_custom_user_model_is_configured(self):
        User = get_user_model()

        self.assertEqual(User._meta.app_label, 'bookshelf')
        self.assertEqual(User._meta.model_name, 'user')

    def test_create_user_and_superuser(self):
        User = get_user_model()

        user = User.objects.create_user(
            email='user@example.com',
            password='test-password-123',
        )

        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.check_password('test-password-123'))

        admin = User.objects.create_superuser(
            email='admin@example.com',
            password='admin-password-123',
        )

        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.check_password('admin-password-123'))


class AddressModelTests(TestCase):
    def test_can_create_address_for_user(self):
        User = get_user_model()

        user = User.objects.create_user(
            email='customer@example.com',
            password='test-password-123',
        )

        address = Address.objects.create(
            user=user,
            street_address='123 Main Street',
            city='São Paulo',
            state='SP',
            postal_code='01000-000',
            country='Brazil',
        )

        self.assertEqual(address.user, user)
        self.assertEqual(address.street_address, '123 Main Street')
        self.assertTrue(address.is_default)
