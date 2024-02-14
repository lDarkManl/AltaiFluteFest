from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from account import services, forms

@login_required
def account(request):
	context = services.get_context_for_account(request)
	return render(request, 'account/account.html', context)

class Register(CreateView):
	model = User
	form_class = forms.AccountRegistrationForm
	template_name = 'account/register.html'
	success_url = reverse_lazy('account:account')

	def form_valid(self, form):
		valid = super().form_valid(form)
		username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
		form_login = services.make_form_for_login(username, password)
		services.login_user_with_form(self.request, form_login)
		return valid

class Login(LoginView):
	model = User
	form_class = forms.AccountLoginForm
	template_name = 'account/login.html'
	
	def get_success_url(self):
		return reverse('account:account')

def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse('account:login'))