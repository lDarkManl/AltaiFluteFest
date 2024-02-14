from django.urls import path
from django.contrib.auth.decorators import login_required
from application import views

app_name = 'application'
urlpatterns = [
	path('create_application/', login_required(views.CreateApplication.as_view()), name='create_application'),
	path('change_application/<int:pk>/', login_required(views.ChangeApplication.as_view()), name='change_application'),
	path('delete_application/<int:pk>/', login_required(views.delete_application_view), name='delete_application'),
]