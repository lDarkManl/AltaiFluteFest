from django.shortcuts import render
from main import services

def index(request):
	context = services.get_context_for_index()
	return render(request, 'main/index.html', context)