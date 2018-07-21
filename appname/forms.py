from django import forms

class PostForm(forms.Form):
    zodiac = forms.CharField()
