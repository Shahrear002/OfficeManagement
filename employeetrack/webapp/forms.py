from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class signupform(forms.Form):
	name = forms.CharField(required=True)
	username = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(signupform, self).clean()
		name = cleaned_data.get('name')
		email = cleaned_data.get('email')
		username = cleaned_data.get('username')
		password = cleaned_data.get('password')
		if not name and not email and not username and not password:
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

class mealform(forms.Form):
	cost = forms.IntegerField(required=True)
	description = forms.CharField(required=True)

	def clean(self):
		cleaned_data = super(mealform, self).clean()
		cost = cleaned_data.get('cost')
		description = cleaned_data.get('description')
		if not cost and not description:
			raise forms.ValidationError('Cost and description field can not be left blank')
