from django import forms


class Gurate(forms.Form):
    time = forms.IntegerField(min_value=10)
