from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='user@example.com', nickname='testuser', password='testpass123')
        self.assertEqual(user.email, 'user@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='admin@example.com', nickname='adminuser', password='admin123')
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
