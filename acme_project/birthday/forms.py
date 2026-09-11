from django import forms

MAX_L = 20


class BirthdayForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=MAX_L)
    last_name = forms.CharField(
        required=False,
        label="Фамилия",
        help_text='Необязательное поле'
    )
    birthday = forms.DateField(
        label='Дата рождения',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
