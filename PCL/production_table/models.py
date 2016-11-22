from django.db import models
from django.utils.timezone import now
from master_table.models import FinishedProductItem, Shift,\
    CPItem, FundamentalProductType, RawItem, Shift, FinishedProductItem

from smart_selects.db_fields import ChainedForeignKey


class ProductionEntry(models.Model):

    fundamental_type = models.ForeignKey(FundamentalProductType)
    # raw_item = models.ForeignKey(RawItem)
    finished_product_item = ChainedForeignKey(
        FinishedProductItem,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )

    # cp_item = models.ForeignKey(CPItem, blank = True, null = True)

    shift = ChainedForeignKey(
        Shift,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    unit_amount = models.FloatField()
    invoice_no = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    # This timefield is added just to keep track of supliers ie log them
    creation_time = models.DateTimeField(default=now, editable=False)
    edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.finished_product_item.name

    class Meta:
        verbose_name = "Final Finished Product Entry"
        verbose_name_plural = "Final Finished Product Entries"


class RawItemEntry(models.Model):

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

    unit_amount = models.FloatField()
    invoice_no = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    # This timefield is added just to keep track of supliers ie log them
    creation_time = models.DateTimeField(default=now, editable=False)
    edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.raw_item.name


    def clean(self):
        if self.creation_time > self.edit_time:
            raise ValidationError('Start date is after end date')

    class Meta:
        verbose_name = "Production Godown Raw Item Entry"
        verbose_name_plural = "Production Godown Raw Items Entry"


class RIIssueEntry(models.Model):

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
    shift = ChainedForeignKey(
        Shift,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    unit_amount = models.FloatField()
    # invoice_no = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    # This timefield is added just to keep track of supliers ie log them
    creation_time = models.DateTimeField(default=now, editable=False)
    edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.raw_item.name

    def clean(self):
        if self.creation_time > self.edit_time:
            raise ValidationError('Start date is after end date')

    class Meta:
        verbose_name = "Raw Item Issued From Gowdown By Shifts"
        verbose_name_plural = "Raw Items Issued From Gowdown By Shifts"



class RIReturnEntry(models.Model):

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
    shift = ChainedForeignKey(
        Shift,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    unit_amount = models.FloatField()
    # invoice_no = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    # This timefield is added just to keep track of supliers ie log them
    creation_time = models.DateTimeField(default=now, editable=False)
    edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.raw_item.name

    def clean(self):
        if self.creation_time > self.edit_time:
            raise ValidationError('Start date is after end date')

    class Meta:
        verbose_name = "Returned Raw Item To Gowdown By Shifts"
        verbose_name_plural = "Returned Raw Items To Gowdown By Shifts"
