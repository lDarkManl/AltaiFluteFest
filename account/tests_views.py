from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()

	def test_account_without_login(self):
		response = self.client.get(reverse('account:account'))

		self.assertEquals(response.status_code, 302)

	def test_account_with_login(self):
		self.user = User.objects.create_user(username='testuser', password='12345')
		self.client.login(username='testuser', password='12345')
		response = self.client.get(reverse('account:account'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'account/account.html')

	def test_register(self):
		response = self.client.get(reverse('account:register'))

		self.assertEquals(response.status_code, 200)

	def test_login(self):
		response = self.client.get(reverse('account:login'))

		self.assertEquals(response.status_code, 200)

	