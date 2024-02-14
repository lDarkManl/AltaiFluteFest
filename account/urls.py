from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
	path('', views.account, name='account'),
	path('login/', views.Login.as_view(), name='login'), 
	path('register/', views.Register.as_view(), name='register'), 
 	path('logout/', views.logout_user, name='logout'),
]