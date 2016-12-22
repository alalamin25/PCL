from django.db import models
from django.utils.timezone import now


class MyModel(models.Model):

    type = models.CharField(verbose_name="Expression", max_length=32)
    action = models.CharField(max_length=32, choices=(('', ''), ))
