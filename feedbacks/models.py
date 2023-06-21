from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from project1.project.mixins.models import PKMixins


class Feedback(PKMixins):
    text = models.TextField()
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    rating = models.PositiveSmallIntegerField(
        validators=(MaxValueValidator(5),)
    )