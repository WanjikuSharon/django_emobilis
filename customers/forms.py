from django import forms

from customers.models import Customers


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'

        widgets= {
            'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your email'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your gender'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your age'}),
        }