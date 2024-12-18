from django import forms

from customers.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets= {
            'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your name'}),
            'admission_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your admission number'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your email'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your gender'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your age'}),
            'image':forms.ClearableFileInput(attrs=
                                             {
                                                 'class': 'form-control',
                                                 'accept': 'images/*',
                                                 'title': 'Upload Your Image'
                                             })
        }