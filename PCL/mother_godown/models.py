from django.db import models
from master_table.models import Suplier, RawItem
from django.utils.timezone import now
from django.core.exceptions import ValidationError

from smart_selects.db_fields import ChainedForeignKey

from master_table.models import FundamentalProductType, RawItem
# from mptt.models import MPTTModel, TreeForeignKey


UNIT_TYPE_CHOICES = (
    ('kg', 'KG'),
    ('ton', 'TON')
)


class PurchaseEntry(models.Model):

    fundamental_type = models.ForeignKey(FundamentalProductType)
    # raw_item = models.ForeignKey(RawItem)
    raw_item = ChainedForeignKey(
        RawItem,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    suplier = models.ForeignKey(Suplier)
    # suplier2 = models.ForeignKey(Suplier)
    unit_price = models.FloatField()

    unit_type = models.CharField(choices=UNIT_TYPE_CHOICES, max_length=30)
    unit_amount = models.FloatField()
    invoice_no = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    # This timefield is added just to keep track of supliers ie log them
    date = models.DateTimeField(default=now)
    # edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.raw_item.name

    class Meta:
        verbose_name = "New Purchase Entry To Mother Godown"
        verbose_name_plural = "New Purchase Entries To Mother Godown"


class IssueEntry(models.Model):

    fundamental_type = models.ForeignKey(FundamentalProductType)
    # raw_item = models.ForeignKey(RawItem)
    raw_item = ChainedForeignKey(
        RawItem,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    unit_type = models.CharField(choices=UNIT_TYPE_CHOICES, max_length=30)
    unit_amount = models.FloatField()
    invoice_no = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    # This timefield is added just to keep track of supliers ie log them
    date = models.DateTimeField(default=now)
    # edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.raw_item.name

    def clean(self):
        if self.creation_time > self.edit_time:
            raise ValidationError('Start date is after end date')

    class Meta:
        verbose_name = "Main Godown To Production Godown Entry Table"
        verbose_name_plural = "Main Godown To Production Godown Entry Table"


# class Dispatch(models.Model):

#     raw_item = models.ForeignKey(RawItem)
#     unit_amount = models.FloatField()
#     invoice_no = models.CharField(max_length=100)
#     comment = models.TextField(blank=True, null=True)

#     # This timefield is added just to keep track of supliers ie log them
#     creation_time = models.DateTimeField(default=now, editable=False)
#     edit_time = models.DateTimeField(default=now, editable=False)

#     def __str__(self):
#         return self.raw_item.name
