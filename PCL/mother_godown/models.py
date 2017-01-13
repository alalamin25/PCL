from django.db import models

from master_table.models import Supplier, RawItem
from django.utils.timezone import now
from django.core.exceptions import ValidationError
# from django.db.models.signals import m2m_changed

from smart_selects.db_fields import ChainedForeignKey

from master_table.models import FundamentalProductType, RawItem, RIMiddleCat, RILowerCat
# from mptt.models import MPTTModel, TreeForeignKey


UNIT_TYPE_CHOICES = (
    ('kg', 'KG'),
    ('ton', 'TON')
)


class PurchaseEntry(models.Model):

    fundamental_type = models.ForeignKey(FundamentalProductType,
                                         blank=True, null=True,)

    middle_category_type = ChainedForeignKey(
        RIMiddleCat,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        blank=True,
        null=True,
        show_all=False,
        auto_choose=True,
        sort=True
    )
    # lower_category_type = models.ForeignKey(FPLowerCat)
    lower_category_type = ChainedForeignKey(
        RILowerCat,
        chained_field="middle_category_type",
        chained_model_field="middle_category_type",
        blank=True,
        null=True,
        show_all=False,
        auto_choose=True,
        sort=True
    )

    raw_item_chained = ChainedForeignKey(
        RawItem,
        chained_field="lower_category_type",
        chained_model_field="lower_category_type",
        related_name='ri_chained',
        blank=True,
        null=True,
        show_all=False,
        auto_choose=True,
        sort=True
    )
    raw_item_many = models.ManyToManyField(
        RawItem, blank=True, related_name='ri_many')

    raw_item = models.ForeignKey(RawItem, blank=True, null=True)
    # supplier = models.ForeignKey(Supplier)
    supplier = models.ManyToManyField(Supplier)
    # suplier2 = models.ForeignKey(Suplier)
    unit_price = models.FloatField()

    unit_type = models.CharField(choices=UNIT_TYPE_CHOICES, max_length=30)
    unit_amount = models.FloatField()
    total_price = models.FloatField()
    invoice_no = models.CharField(max_length=100, blank=True, null=True)
    enroll_comment_in_report = models.BooleanField(
        "Enroll This Comment In Report:", default=False)
    comment = models.TextField(blank=True, null=True)

    # This timefield is added just to keep track of supliers ie log them
    date = models.DateTimeField(default=now)
    # edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):

        if(self.raw_item):
            return self.raw_item.name
        else:
            return "No Raw Item Selected"

    # def clean(self, *args, **kwargs):

    #     if self.supplier.count() > 1:
    #         print("\n supplier count: ")
    #         print(self.supplier.count())
    #         raise ValidationError("You can't assign more than 1 Supplier")
    #     super(PurchaseEntry, self).clean(*args, **kwargs)

    # def regions_changed(sender, **kwargs):
    #     if kwargs['instance'].supplier.count() > 1:
    #         raise ValidationError("You can't assign more than three regions")

    # m2m_changed.connect(regions_changed, sender=PurchaseEntry.through)

    class Meta:
        verbose_name = "New Purchase Entry To Mother Godown"
        verbose_name_plural = "New Purchase Entries To Mother Godown"


class IssueEntry(models.Model):

    fundamental_type = models.ForeignKey(FundamentalProductType,
                                         blank=True, null=True,)

    middle_category_type = ChainedForeignKey(
        RIMiddleCat,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        blank=True,
        null=True,
        show_all=False,
        auto_choose=True,
        sort=True
    )
    # lower_category_type = models.ForeignKey(FPLowerCat)
    lower_category_type = ChainedForeignKey(
        RILowerCat,
        chained_field="middle_category_type",
        chained_model_field="middle_category_type",
        blank=True,
        null=True,
        show_all=False,
        auto_choose=True,
        sort=True
    )

    raw_item_chained = ChainedForeignKey(
        RawItem,
        chained_field="lower_category_type",
        chained_model_field="lower_category_type",
        related_name='raw_item_chained',
        blank=True,
        null=True,
        show_all=False,
        auto_choose=True,
        sort=True
    )
    raw_item = models.ForeignKey(RawItem, blank=True, null=True)

    raw_item_many = models.ManyToManyField(
        RawItem, blank=True, related_name='raw_item_many')

    unit_type = models.CharField(choices=UNIT_TYPE_CHOICES, max_length=30)
    unit_amount = models.FloatField()
    invoice_no = models.CharField(max_length=100, blank=True, null=True)
    enroll_comment_in_report = models.BooleanField(
        "Enroll This Comment In Report:", default=False)
    comment = models.TextField(blank=True, null=True)

    # This timefield is added just to keep track of supliers ie log them
    date = models.DateTimeField(default=now)
    # edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):

        if(self.raw_item):
            return self.raw_item.name
        else:
            return "No Raw Item Selected"

    # def get_name(self):
    #     if(self.raw_item_many):
    #         raw_item =

    # def clean(self):
    #     if self.creation_time > self.edit_time:
    #         raise ValidationError('Start date is after end date')

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
