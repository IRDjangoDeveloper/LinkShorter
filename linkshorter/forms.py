from django import forms

class userlink(forms.Form):
    input = forms.URLField(widget=forms.URLInput(attrs={'class':'form-control'}))