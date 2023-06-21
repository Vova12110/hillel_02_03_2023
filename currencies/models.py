from django.db import models

from project1.project.constants import MAX_DIGITS, DECIMAL_PLACES
from project1.project.mixins.models import PKMixins
from project1.model_choices import Currencies


class CurrencyHistory(PKMixins):
    code = models.CharField(
        max_length=16,
        choices=Currencies.choices,
        default=Currencies.UAH
    )
    buy = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        default=1
    )
    sale = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        default=1
    )

    def __str__(self):
        return f"{self.code} - {self.buy} / {self.sale}"