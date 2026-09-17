from datetime import date

# Импортируем ошибку валидации.
from django.core.exceptions import ValidationError


# На вход функция будет принимать дату рождения.
def real_age(value: date) -> None:
    # и делим на 365.
    age = (date.today() - value).days / 365
    if age < 1 or age > 120:
        raise ValidationError(
            'Ожидается возраст от 1 года до 120 лет'
        )
