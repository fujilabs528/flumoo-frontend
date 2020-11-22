from django import forms

class SearchForm(forms.Form):
    q= forms.CharField(label="search", max_length=50)