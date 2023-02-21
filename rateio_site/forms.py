from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cost_Center, Product

class Cost_Center_Form(forms.ModelForm):
	class Meta:
		model = Cost_Center
		fields = "__all__"

	def __init__ (self, *args, **kwargs):
			super().__init__(*args, **kwargs)

			#self.fields['desc_cost_center'].widget.attrs['class'] = 'form-control'

class Product_Form(forms.ModelForm):
	class Meta:
		model = Product
		fields = "__all__"

	def __init__ (self, *args, **kwargs):
			super().__init__(*args, **kwargs)

class Sign_Up_Form (UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=512)
	last_name = forms.CharField(max_length=512)
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


