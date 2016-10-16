from django.db import models
from django.utils.timezone import now
# Create your models here.


class Suplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone1 = models.CharField(max_length=30)
    phone2 = models.CharField(max_length=30)
    phone3 = models.CharField(max_length=30)
    phone4 = models.CharField(max_length=30)
    phone5 = models.CharField(max_length=30)
    # This timefield is added just to keep track of supliers ie log them
    creation_time = models.DateTimeField(default=now, editable=False)
    edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        edit_time = now
