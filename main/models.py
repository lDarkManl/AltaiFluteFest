from django.db import models

def file_directory_path(instance, filename):
	return f"{instance.artist.id}/{filename}"

def artist_photo_path(instance, filename):
	return f"{filename}"

class Artist(models.Model):
	name = models.CharField('Имя', max_length=255)
	photo = models.ImageField('Фото артиста', upload_to=artist_photo_path)
	description = models.TextField('Описание')

class ArtistMedia(models.Model):
	'''Модель фото/видео для артиста'''
	file = models.FileField(upload_to=file_directory_path)
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='artist', related_name='file')