from main.models import Artist, ArtistMedia

def get_context_for_index():
	context = {}
	context['artists'] = Artist.objects.all()
	return context
