from django import forms
import os

class settingsForm(forms.Form):
    database = forms.CharField(max_length=100)
    training = forms.CharField(max_length=100)
    alg = forms.CharField(max_length=100)
    norm = forms.CharField(max_length=100)
