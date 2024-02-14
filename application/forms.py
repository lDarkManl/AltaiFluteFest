from django import forms
from application.models import Application, Package

class ApplicationForm(forms.ModelForm):
	class Meta:
		model = Application
		fields = ('name', 'age', 'email', 'phone_number', 'country', 'employment', 'package')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['package'] = forms.ModelChoiceField(queryset=Package.objects.all(), widget=forms.RadioSelect())