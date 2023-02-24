import datetime

from django.core.exceptions import ValidationError


def validate_starte_date(value):
    now = datetime.datetime.now().date()
    if value < now:
        raise ValidationError(f"Выбранная дата должна быть больше либо равна {now.strftime('%d.%m.%Y')}")
