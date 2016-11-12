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

    class ReportBuilder:
        fields = ('name',)   # Explicitly allowed fields


class FundamentalProductType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RawItemMiddleCategory(models.Model):
    name = models.CharField(max_length=100)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class RawItemLowerCategory(models.Model):
    name = models.CharField(max_length=100)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    middle_category_type = models.ForeignKey(RawItemMiddleCategory)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class RawItem(models.Model):
    name = models.CharField(max_length=100)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    middle_category_type = models.ForeignKey(RawItemMiddleCategory)
    lower_category_type = models.ForeignKey(RawItemLowerCategory)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class FinishedProductItemMiddleCategory(models.Model):
    name = models.CharField(max_length=100)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class FinishedProductItemLowerCategory(models.Model):
    name = models.CharField(max_length=100)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    middle_category_type = models.ForeignKey(FinishedProductItemMiddleCategory)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class FinishedProductItem(models.Model):
    name = models.CharField(max_length=100)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    middle_category_type = models.ForeignKey(FinishedProductItemMiddleCategory)
    lower_category_type = models.ForeignKey(FinishedProductItemLowerCategory)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class CompoundProductionItem(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    type = models.ForeignKey(FundamentalProductType)

    def __str__(self):
        return self.name


class CompoundProductionItemEntry(models.Model):
    compound_production_item = models.ForeignKey(CompoundProductionItem)
    production_item = models.ForeignKey(FinishedProductItem)
    unit_amount = models.FloatField()

    def __str__(self):
        return self.compound_production_item.name


class Shift(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
