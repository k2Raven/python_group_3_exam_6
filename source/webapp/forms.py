from django import forms
from django.forms import widgets


class RecordForm(forms.Form):
    author = forms.CharField(max_length=40, required=True, label='Name')
    email_author = forms.EmailField(max_length=60, required=True, label='Email Address')
    text = forms.CharField(max_length=3000, required=True, label='Text', widget=widgets.Textarea)


class SearchForm(forms.Form):
    query = forms.CharField(required=True)