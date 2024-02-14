from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib import messages
from django.template.loader import get_template
from django.core.exceptions import ValidationError
from application.models import Application, Package
from application.forms import ApplicationForm

def get_context_for_create():
	'''Получить контекст для создания заявки'''
	context = {}
	context['application_form'] = ApplicationForm()
	context['packages'] = Package.objects.all()
	return context

def get_context_for_change(primary_key):
	'''Получить контекст для изменения заявки'''
	context = {}
	unchanged_application = get_object_or_404(Application, pk=primary_key)
	context['application_form'] = ApplicationForm(instance=unchanged_application)
	context['packages'] = Package.objects.all()
	return context

def delete_application(primary_key):
	'''Удалить заявку'''
	instance = get_object_or_404(Application, pk=primary_key)
	instance.delete()

def send_email(variant):
	'''Отправить email'''
	to_email = 'd_gusev_04@mail.ru'
	from_email = 'dimon_gusev_22@mail.ru'
	subject = 'Заявка'
	context = {
		'message': variant
	}
	html_content = get_template(f'mails/email.html').render(context)
	msg = EmailMultiAlternatives(subject, '', from_email, [to_email])
	msg.attach_alternative(html_content, "text/html")
	msg.send()

def save_application_or_return_form(request):
	'''Сохранить заявку или, если форма не прошла проверку, вернуть форму'''
	form = ApplicationForm(request.POST)
	if form.is_valid():
		application_object = form.save(commit=False)
		application_object.account = request.user
		application_object.save()
	else:
		return form

def change_application_or_return_form(request, primary_key):
	'''Изменить заявку или, если форма не прошла проверку, вернуть форму'''
	application = get_object_or_404(Application, pk=primary_key)
	form = ApplicationForm(request.POST, instance=application)
	if form.is_valid():
		form.save()
	else:
		return form


