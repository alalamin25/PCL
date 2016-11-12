from django.db import models
from master_table.models import Suplier, RawItem
from django.utils.timezone import now
from django.core.exceptions import ValidationError


class Purchase(models.Model):

    raw_item = models.ForeignKey(RawItem)
    suplier = models.ForeignKey(Suplier)
    unit_price = models.FloatField()
    unit_amount = models.FloatField()
    invoice_no = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)

    # This timefield is added just to keep track of supliers ie log them
    creation_time = models.DateTimeField(default=now, editable=False)
    edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.raw_item.name




class Issue(models.Model):

    raw_item = models.ForeignKey(RawItem)
    unit_amount = models.FloatField()
    invoice_no = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)

    # This timefield is added just to keep track of supliers ie log them
    creation_time = models.DateTimeField(default=now, editable=False)
    edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.raw_item.name

    def clean(self):
        if self.creation_time > self.edit_time:
            raise ValidationError('Start date is after end date')


class Dispatch(models.Model):

    raw_item = models.ForeignKey(RawItem)
    unit_amount = models.FloatField()
    invoice_no = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)

    # This timefield is added just to keep track of supliers ie log them
    creation_time = models.DateTimeField(default=now, editable=False)
    edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.raw_item.name
