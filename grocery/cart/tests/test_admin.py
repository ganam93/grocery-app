# from django.test import TestCase, Client
# from django.contrib.auth import get_user_model
# from django.urls import reverse


# class AdminSiteTests(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.admin_user = get_user_model().objects.create_superuser(
#             email='admin@ganam.com',
#             password='admin@123'
#         )
#         self.client.force_login(self.admin_user)
#         self.user = get_user_model.objects.create_user(
#             email='test@ganam.com',
#             password='user@123',
#             name='Test user  full name'
#         )

#     def test_users_listed(self):
#         """Test that users are listed on user page"""
#         url = reverse('admin:cart_user_changelist')
#         res = self.client.get_user_model(url)
        
#         self.assertContains(res, self.user.name)
#         self.assertContains(res, self.user.email)
