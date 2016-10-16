from django.db import models
from django.utils.timezone import now
# Create your models here.


class Suplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone1 = models.CharField(max_length=30, blank=True, null=True)
    phone2 = models.CharField(max_length=30, blank=True, null=True)
    phone3 = models.CharField(max_length=30, blank=True, null=True)
    phone4 = models.CharField(max_length=30, blank=True, null=True)
    phone5 = models.CharField(max_length=30, blank=True, null=True)
    # This timefield is added just to keep track of supliers ie log them
    creation_time = models.DateTimeField(default=now, editable=False)
    edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name


class FundamentalProductType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RawItem(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    type = models.ForeignKey(FundamentalProductType)

    def __str__(self):
        return self.name
