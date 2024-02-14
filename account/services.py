from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from account.forms import AccountLoginForm
from application.models import Application

def login_user_with_form(request, form):
	'''Войти в аккаунт, используя форму с аккаунтом'''
	new_user = authenticate(username=form['username'].value(), password=form['password'].value())
	login(self.request, new_user)

def make_form_for_login(username, password):
	'''Подготовить форму для входа, используя логин и пароль'''
	form = AccountLoginForm(initial={'username': username, 'password': password})
	return form

def get_context_for_account(request):
	context = {}
	context['application'] = get_object_or_none(Application, request.user.id)
	return context

def get_object_or_none(model, primary_key):
	'''Returns object or handles ObjectDoesNotExist exception and returns None'''
	try:
		obj = model.objects.get(account_id=primary_key)
	except ObjectDoesNotExist:
		return None
	else:
		return obj