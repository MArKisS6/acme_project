from django.db import models

MAX_L = 20


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=MAX_L)
    last_name = models.CharField(
        'Фамилия',
        blank=True,
        help_text='Необязательное поле',
        max_length=MAX_L
    )
    birthday = models.DateField('Дата рождения')
