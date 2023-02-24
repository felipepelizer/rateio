from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cost_Center, Product, Employee, Squad


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
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


class Employee_Form(forms.ModelForm):
	class Meta:
		model = Employee
		fields = "__all__"

	def __init__ (self, *args, **kwargs):
			super().__init__(*args, **kwargs)

class Squad_Form(forms.ModelForm):
	class Meta:
		model = Squad
		fields = "__all__"

	def __init__ (self, *args, **kwargs):
			super().__init__(*args, **kwargs)