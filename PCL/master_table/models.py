from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
import random
from smart_selects.db_fields import ChainedForeignKey


UNIT_TYPE_CHOICES = (
    ('kg', 'KG'),
    ('ton', 'TON')
)


def get_unique_code(id):
    return 'code_' + str(id)


class Code(models.Model):

    supplier_code = models.CharField(
        "Supplier Code: ", max_length=3)
    customer_code = models.CharField(
        "Customer Code: ", max_length=3)
    bank_code = models.CharField(
        "Bank Code: ", max_length=3)

    deport_code = models.CharField(
        "Depot Code: ", max_length=3)

    def clean(self, *args, **kwargs):

        if Code.objects.all().count() > 1:
            # print("\n supplier count: ")
            # print(self.supplier.count())
            raise ValidationError("You can't create more than 1 code instance")
        super(Code, self).clean(*args, **kwargs)


class Bank(models.Model):
    name = models.CharField("Bank Name", max_length=100)
    # address = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=5, unique=True, blank=True, null=True)
    # account_no = models.ManyToManyField(BankAccount)

    def __str__(self):
        return self.name


class BankAccount(models.Model):
    name = models.CharField("Bank Account Number:", max_length=100)
    bank = models.ForeignKey(
        Bank,  to_field='code', verbose_name="Select Bank")
    # address = models.TextField(blank=True, null=True)
    # code = models.CharField(max_length=30, unique=True)

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
    code = models.CharField(max_length=5, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Depot"
        verbose_name_plural = "Depotes"



class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=5, unique=True, blank=True, null=True)
    deport = models.ForeignKey(Deport, verbose_name='Depot')

    def __str__(self):
        return self.code + ' ' + self.deport.name + ' ' + self.name


class FundamentalProductType(models.Model):
    name = models.CharField(max_length=50)
    fp_code = models.CharField(
        "Finished Product Code:", max_length=1, unique=True)
    ri_code = models.CharField("Raw Item Code:", max_length=1, unique=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):

    name = models.CharField(max_length=100)
    fundamental_type = models.ManyToManyField(FundamentalProductType)
    # Customer = models.ForeignKey(Customer)
    code = models.CharField(max_length=5, unique=True, blank=True, null=True)
    address = models.TextField()
    phone1 = models.CharField(max_length=30, blank=True, null=True)
    phone2 = models.CharField(max_length=30, blank=True, null=True)
    phone3 = models.CharField(max_length=30, blank=True, null=True)
    phone4 = models.CharField(max_length=30, blank=True, null=True)
    phone5 = models.CharField(max_length=30, blank=True, null=True)
    # This timefield is added just to keep track of supliers ie log them
    # creation_time = models.DateTimeField(default=now, editable=False)
    # edit_time = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name

    # def get_unique_code(self):
    #     return 'code_' + str(id)


class RIMiddleCat(models.Model):
    name = models.CharField("RawItem Middle Category Name:", max_length=100)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    code = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Raw Item Middle Category"
        verbose_name_plural = "Raw Item Middle Categories"


class RILowerCat(models.Model):
    name = models.CharField("Raw Item Lower Category Name:", max_length=100)
    code = models.CharField(max_length=1, unique=True)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    # middle_category_type = models.ForeignKey(FinishedProductItemMiddleCategory)
    middle_category_type = ChainedForeignKey(
        RIMiddleCat,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Raw Item  Lower Category"
        verbose_name_plural = "Raw Item Lower Categories"


class RawItem(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5, unique=True, blank=True, null=True)
    fundamental_type = models.ForeignKey(FundamentalProductType)

    middle_category_type = ChainedForeignKey(
        RIMiddleCat,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    # lower_category_type = models.ForeignKey(FPLowerCat)
    lower_category_type = ChainedForeignKey(
        RILowerCat,
        chained_field="middle_category_type",
        chained_model_field="middle_category_type",
        show_all=False,
        auto_choose=True,
        sort=True
    )

    grade = models.CharField(max_length=50, blank=True, null=True)

    def get_name(self):
        return self.code + ": " + self.name
    get_name.short_description = 'Name & Code'

    def __str__(self):
        return self.code + ": " + self.name
        # return self.name


class FPMiddleCat(models.Model):
    name = models.CharField("Middle Category Name:", max_length=100)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    code = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return self.name

    @property
    def get_code(self):
        return "code"
        return self.fundamental_type.fp_code + self.code
    # get_code.short_description = 'Full Code'

    class Meta:
        verbose_name = "Finished Product Item Middle Category"
        verbose_name_plural = "Finished Product Item Middle Categories"

    # class Meta(object):
    #     unique_together = ('code',)


class FPLowerCat(models.Model):
    name = models.CharField("Lower Category Name:", max_length=100)
    code = models.CharField(max_length=1, unique=True)
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
    # comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_code(self):
        return self.fundamental_type.fp_code + self.middle_category_type.code + self.code
    get_code.short_description = 'Full Code'

    class Meta:
        verbose_name = "Finished Product Item Lower Category"
        verbose_name_plural = "Finished Product Item Lower Categories"


class FPItem(models.Model):

    name = models.CharField(
        "Finished Product Name:", max_length=100, unique=True)
    code = models.CharField(max_length=5, unique=True, blank=True, null=True)
    unit_price = models.FloatField(default=0)
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
    # comment = models.TextField(blank=True, null=True)
    is_cp = models.BooleanField("Is Compound Item", default=False)
    # comment2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.code + ": " + self.name

    class Meta:
        verbose_name = "Finished Product Item "
        verbose_name_plural = "Finished Product Items"


class CPItem(models.Model):
    # name = models.CharField(max_length=100)
    fp_item = models.ForeignKey(FPItem, verbose_name="Select Compound Product")
    # comment = models.TextField(blank=True, null=True)

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
    unit_type = models.CharField(choices=UNIT_TYPE_CHOICES, max_length=30)
    unit_amount = models.FloatField()

    def __str__(self):
        return self.cp_item.fp_item.name

    def clean(self, *args, **kwargs):
        if (self.finished_production_item.is_cp):
            raise ValidationError(
                'A Compound Item cant consist of another compound Item')
        super(CPItemEntry, self).clean(*args, **kwargs)


class Shift(models.Model):
    name = models.CharField(max_length=100)
    fundamental_type = models.ForeignKey(FundamentalProductType)
    # comment = models.TextField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name


# class Color(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name
