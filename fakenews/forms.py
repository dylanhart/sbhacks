from django import forms

class DetectForm(forms.Form):
    url = forms.URLField()

