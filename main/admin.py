from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from main.models import Artist, ArtistMedia

class ArtistMediaAdmin(admin.StackedInline):
	model = ArtistMedia

@admin.register(Artist)
class ArtistAdmin(TranslationAdmin):
	inlines = [ArtistMediaAdmin]

	class Meta:
		model = Artist
