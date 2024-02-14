from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from application.models import Application, Package
from application.forms import ApplicationForm

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='testuser', password='12345')
		self.client.login(username='testuser', password='12345')
		self.package = Package.objects.create(name='test')
		self.application = Application.objects.create(
			account=self.user, 
			name='test',
			age=18,
			email='test@mail.ru', 
			phone_number='9876543210', 
			country='test',  
			employment='test', 
			package=self.package, 
			status=Application.status_list[0][0]
		)
		self.data = {
			'name':'test1', 
			'email':'test@mail.ru', 
			'phone_number':'9876543210', 
			'country':'test', 
			'locality':'test', 
			'employment':'test', 
			'package':self.package, 
		}
		
	def test_create_application_get(self):
		response = self.client.get(reverse('application:create_application'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'application/create_application.html')

	def test_change_application_get(self):
		response = self.client.get(reverse('application:change_application', args=[self.application.id]))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'application/change_application.html')

	def test_create_application_post(self):
		response = self.client.post(reverse('application:create_application'), data=self.data)

		self.assertEquals(response.status_code, 200)


