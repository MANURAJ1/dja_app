from  django import forms

class Formname(forms.Form):
    name=forms.CharField()
    db=forms.Select()
    # name=forms.Select(widget=forms.HiddenInput)

