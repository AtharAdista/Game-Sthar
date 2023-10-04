from django import forms
from main.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description","category", "platform", "amount" ,"price"]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-1 focus:ring-indigo-600 rounded-md'}),
            'description': forms.TextInput(attrs={'class': 'border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-1 focus:ring-indigo-600 rounded-md'}),
            'platform': forms.TextInput(attrs={'class': 'border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-1 focus:ring-indigo-600 rounded-md'}),
            'category': forms.TextInput(attrs={'class': 'border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-1 focus:ring-indigo-600 rounded-md'}),
            'amount': forms.NumberInput(attrs={'class': 'border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-1 focus:ring-indigo-600 rounded-md'}),
            'price': forms.NumberInput(attrs={'class': 'border w-full h-5 px-3 py-5 mt-2 hover:outline-none focus:outline-none focus:ring-1 focus:ring-indigo-600 rounded-md'}),
           
        }
    
