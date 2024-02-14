from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from application import services

'''GET: Создание и изменение: получение контекста и рендер'''
'''POST: Обработка: Проверка формы, запись ее в бд и отправка на почту'''

class CreateApplication(View):

	def get(self, request):
		context = services.get_context_for_create()
		return render(request, 'application/create_application.html', context)

	def post(self, request):
		form = services.save_application_or_return_form(request)
		if form:
			context = services.get_context_for_create()
			context['application_form'] = form
			return render(request, 'application/create_application.html', context)
		services.send_email('create')
		return HttpResponseRedirect(reverse('account:account'))
		
class ChangeApplication(View):

	def get(self, request, pk):
		context = services.get_context_for_change(pk)
		context['pk'] = pk
		return render(request, 'application/change_application.html', context)

	def post(self, request, pk):
		form = services.change_application_or_return_form(request, pk)
		if form:
			context = services.get_context_for_change(pk)
			context['application_form'] = form
			return render(request, 'application/change_application.html', context)
		services.send_email('change')
		return HttpResponseRedirect(reverse('account:account'))

'''Удаление: Удаление записи из бд и отправка на почту'''

def delete_application_view(request, pk):
	services.delete_application(pk)
	services.send_email('delete')
	return HttpResponseRedirect(reverse('account:account'))

