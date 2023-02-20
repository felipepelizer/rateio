from django import forms
from .models import Cost_Center, Product

class Cost_Center_Form(forms.ModelForm):

	class Meta:
		model = Cost_Center
		fields = "__all__"

	def __init__ (self, *args, **kwargs):
			super().__init__(*args, **kwargs)

class Product_Form(forms.ModelForm):

	class Meta:
		model = Product
		fields = "__all__"

	def __init__ (self, *args, **kwargs):
			super().__init__(*args, **kwargs)


