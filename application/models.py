from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Application(models.Model):
	'''Модель заявки'''
	status_list = [
		('100', 'Заявка не подана'),
		('200', 'В обработке'),
		('300', 'Заявка одобрена'),
		('400', 'Заявка удалена')
	]
	participate_types = [
		('P', 'Участник'),
		('A', 'Сопровождающий')
	]
	account = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Account', related_name='application')
	name = models.CharField('ФИО', max_length=255)
	age = models.IntegerField('Возраст')
	phone_number = PhoneNumberField(region='RU')
	email = models.EmailField('Электронная почта')
	country = models.CharField('Страна, город', max_length=100)
	employment = models.CharField('Место работы/учебы', max_length=100)
	package = models.ForeignKey('Package', on_delete=models.PROTECT, verbose_name='package', related_name='application')
	status = models.CharField('Статус', choices=status_list, max_length=3, default='200')
	type_participant = models.CharField('Тип участия', choices=participate_types, max_length=1, default='P')

	class Meta:
		verbose_name = 'Заявка'
		verbose_name_plural = 'Заявки'

	def __str__(self):
		return self.name

class Package(models.Model):
	name = models.CharField('Название пакета', max_length=100)

class PackageType(models.Model):
	'''Модель варианта фестиваля'''
	package_types = [
		('MIN', 'МИН'),
		('BAS', 'БАЗА'),
		('MAX', 'МАКС'),
	]
	description = models.TextField('Описание пакета')
	price = models.IntegerField('Цена')
	package_type = models.CharField('Тип пакета', choices=package_types, max_length=3, default='MIN')
	package = models.ForeignKey(Package, on_delete=models.CASCADE, verbose_name='package', related_name='package_type')

	class Meta:
		verbose_name = 'Пакет'
		verbose_name_plural = 'Пакеты'

class PackagePhoto(models.Model):
	'''Модель фото для пакета'''
	image = models.ImageField('Фото', upload_to = 'images/%Y/%m/%d/')
	package_type = models.ForeignKey(PackageType, on_delete=models.CASCADE, verbose_name='package_type', related_name='photo')

	class Meta:
		verbose_name = 'Фотография'
		verbose_name_plural = 'Фотографии'

