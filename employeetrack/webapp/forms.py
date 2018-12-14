from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class signupform(forms.Form):
	name = forms.CharField(required=True)
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(signupform, self).clean()
		name = cleaned_data.get('name')
		username = cleaned_data.get('username')
		password = cleaned_data.get('password')
		if not name and not username and not password and not address and not contactnumber:
			raise forms.ValidationError('You have to write something')

class loginform(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(signupform, self).clean()
		username = cleaned_data.get('username')
		password = cleaned_data.get('password')
		if not username and not password:
			raise forms.ValidationError('You have to write something')
