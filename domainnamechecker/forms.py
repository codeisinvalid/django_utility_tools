from django import forms

class DomainSearchForm(forms.Form):
    domain_name = forms.CharField(
        label="Domain Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class':'form-control form-control-lg',
            'placeholder':'Enter a domain name (e.g., example.com)'
        })
    )
    