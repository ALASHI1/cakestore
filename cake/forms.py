from django import forms 
from .models import *
class ContactCreateForm(forms.ModelForm): 
	class Meta:
		model = Contact
		fields = ['name','email','body']

class Adminmage(forms.ModelForm): 
	class Meta:
		model = ProductImage
		fields = ['product','images','images1','images2','images3']

class Adminpage(forms.ModelForm): 
	class Meta:
		model = Category
		fields = ['name','slug']

	class Meta:
		model = Product
		fields = ['category','name','slug','image','description','price','available']
	
