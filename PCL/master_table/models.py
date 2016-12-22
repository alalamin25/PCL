from django.db import models
from django.utils.timezone import now

from smart_selects.db_fields import ChainedForeignKey


class Bank(models.Model):
    name = models.CharField("Bank Name", max_length=100)
    # address = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=30, unique=True)
    # account_no = models.ManyToManyField(BankAccount)

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    name = models.CharField("Bank Account Number:", max_length=100)
    bank = models.ForeignKey(Bank,  to_field='code', verbose_name="Select Bank")
    # address = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class ExpenseCriteria(models.Model):
    name = models.CharField(max_length=100)
    # address = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Deport(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=30, unique=True)
    deport_code = models.ForeignKey(Deport, to_field='code')

    def __str__(self):
        return self.name


class FundamentalProductType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


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

    class ReportBuilder:
        fields = ('name',)   # Explicitly allowed fields


# class FundamentalProductType(models.Model):
#     name = models.CharField(max_length=50)
#     phone1 = models.CharField(max_length=30, blank=True, null=True)
#     def __str__(self):
#         return self.name


class RawItem(models.Model):
    name = models.CharField(max_length=100)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    # middle_category_type = models.ForeignKey(RIMiddleCat)
    # lower_category_type = models.ForeignKey(RILowerCat)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class FPMiddleCat(models.Model):
    name = models.CharField(max_length=100)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Finished Product Item Middle Category"
        verbose_name_plural = "Finished Product Item Middle Categories"


class FPLowerCat(models.Model):
    name = models.CharField(max_length=100)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    # middle_category_type = models.ForeignKey(FinishedProductItemMiddleCategory)
    middle_category_type = ChainedForeignKey(
        FPMiddleCat,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Finished Product Item Lower Category"
        verbose_name_plural = "Finished Product Item Lower Categories"


class FPItem(models.Model):
    name = models.CharField(max_length=100)
    # name = models.CharField(max_length=100)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    # middle_category_type = models.ForeignKey(FPMiddleCat)
    middle_category_type = ChainedForeignKey(
        FPMiddleCat,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    # lower_category_type = models.ForeignKey(FPLowerCat)
    lower_category_type = ChainedForeignKey(
        FPLowerCat,
        chained_field="middle_category_type",
        chained_model_field="middle_category_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    comment = models.TextField(blank=True, null=True)
    is_cp = models.BooleanField("Is Compound Item", default=False)
    # comment2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Finished Product Item "
        verbose_name_plural = "Finished Product Items"


class CPItem(models.Model):
    # name = models.CharField(max_length=100)
    fp_item = models.ForeignKey(FPItem, verbose_name="Select Compound Product")
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fp_item.name

    class Meta:
        verbose_name = "Compound Product Item"
        verbose_name_plural = "Compound Product Items"


class CPItemEntry(models.Model):

    cp_item = models.ForeignKey(CPItem)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    # middle_category_type = models.ForeignKey(FPMiddleCat)
    middle_category_type = ChainedForeignKey(
        FPMiddleCat,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    # lower_category_type = models.ForeignKey(FPLowerCat)
    lower_category_type = ChainedForeignKey(
        FPLowerCat,
        chained_field="middle_category_type",
        chained_model_field="middle_category_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    # production_item = models.ForeignKey(FinishedProductItem)
    finished_production_item = ChainedForeignKey(
        FPItem,
        chained_field="lower_category_type",
        chained_model_field="lower_category_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    unit_amount = models.FloatField()

    def __str__(self):
        return self.cp_item.fp_item.name


class Shift(models.Model):
    name = models.CharField(max_length=100)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    comment = models.TextField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name


# class Color(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name
