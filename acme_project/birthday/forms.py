from django import forms

from .models import Birthday

MAX_L = 20


class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
