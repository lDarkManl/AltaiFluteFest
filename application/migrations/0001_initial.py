# Generated by Django 4.2.8 on 2024-02-06 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название пакета')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Название пакета')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Название пакета')),
            ],
        ),
        migrations.CreateModel(
            name='PackageType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание пакета')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание пакета')),
                ('description_en', models.TextField(null=True, verbose_name='Описание пакета')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('package_type', models.CharField(choices=[('MIN', 'МИН'), ('BAS', 'БАЗА'), ('MAX', 'МАКС')], default='MIN', max_length=3, verbose_name='Тип пакета')),
                ('package_type_ru', models.CharField(choices=[('MIN', 'МИН'), ('BAS', 'БАЗА'), ('MAX', 'МАКС')], default='MIN', max_length=3, null=True, verbose_name='Тип пакета')),
                ('package_type_en', models.CharField(choices=[('MIN', 'МИН'), ('BAS', 'БАЗА'), ('MAX', 'МАКС')], default='MIN', max_length=3, null=True, verbose_name='Тип пакета')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_type', to='application.package', verbose_name='package')),
            ],
            options={
                'verbose_name': 'Пакет',
                'verbose_name_plural': 'Пакеты',
            },
        ),
        migrations.CreateModel(
            name='PackagePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Фото')),
                ('package_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='application.packagetype', verbose_name='package_type')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('country', models.CharField(max_length=100, verbose_name='Страна, город')),
                ('employment', models.CharField(max_length=100, verbose_name='Место работы/учебы')),
                ('status', models.CharField(choices=[('100', 'Заявка не подана'), ('200', 'В обработке'), ('300', 'Заявка одобрена'), ('400', 'Заявка удалена')], default='100', max_length=3, verbose_name='Статус')),
                ('type_participant', models.CharField(choices=[('P', 'Участник'), ('A', 'Сопровождающий')], default='P', max_length=1, verbose_name='Тип участия')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='application', to=settings.AUTH_USER_MODEL, verbose_name='Account')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='application', to='application.package', verbose_name='package')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
