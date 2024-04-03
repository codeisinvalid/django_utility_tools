from django import forms

class UrlShortenForm(forms.Form):
    domain_name = forms.CharField(
        label="Url Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class':'form-control form-control-lg',
            'placeholder':'Enter a url to shorten'
        })
    )
    