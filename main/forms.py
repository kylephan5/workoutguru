from django import forms


class Gurate(forms.Form):
    email = forms.EmailField()
    time = forms.IntegerField(min_value=10)
