from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
	"""docstring for RestaurantForm"""
	class Meta:
		"""docstring for Meta"""
		model = Restaurant
		fields = '__all__'
		# fields = ['name', 'description', 'opening_time', 'closing_time']
			
		