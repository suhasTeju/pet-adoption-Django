from django import forms
from .models import Pizza

class PizzaForm(forms.ModelForm):

    class Meta:
        model=Pizza
        fields=['toppping1','toppping2','size']

class MultipleForm(forms.Form):
    number=forms.IntegerField(min_value=2,max_value=6)
