from modeltranslation.translator import register, TranslationOptions
from main.models import Artist

@register(Artist)
class ArtistTranslationOptions(TranslationOptions):
	fields = ('name', 'description')


