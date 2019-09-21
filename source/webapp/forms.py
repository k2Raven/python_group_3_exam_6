from django import forms
from django.forms import widgets


class RecordForm(forms.Form):
    email_author = forms.EmailField(max_length=60, required=True, label='Email Address')
    author = forms.CharField(max_length=40, required=True, label='Name')
    text = forms.CharField(max_length=3000, required=True, label='Text',
                           widget=widgets.Textarea)