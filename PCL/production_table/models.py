from django.db import models
from django.utils.timezone import now
from master_table.models import FPItem, Shift,\
    FundamentalProductType, RawItem, Shift, FPItem

from smart_selects.db_fields import ChainedForeignKey


class ProductionEntry(models.Model):

    fundamental_type = models.ForeignKey(FundamentalProductType)
    # raw_item = models.ForeignKey(RawItem)
    finished_product_item = ChainedForeignKey(
        FPItem,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank = True,
        null = True,
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
        if(self.finished_product_item):
            return self.finished_product_item.name
        elif(self.cp_item):
            return self.cp_item.name
            
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
        verbose_name = "Issued From Gowdown By Shifts"
        verbose_name_plural = "Issued From Gowdown By Shifts"



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
        verbose_name = "Returned To Gowdown"
        verbose_name_plural = "Returned To Gowdown"
