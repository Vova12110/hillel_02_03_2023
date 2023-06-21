from django.db import models

from project1.project.mixins.models import PKMixins


class Tracking(PKMixins):
    method = models.CharField(max_length=16)
    url = models.CharField(max_length=255)
    data = models.JSONField(default=dict)