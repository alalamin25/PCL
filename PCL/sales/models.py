from django.db import models
from django.utils.timezone import now
from master_table.models import Deport, Customer, FPItem, ExpenseCriteria,\
    Bank, BankAccount, FundamentalProductType, FPMiddleCat, FPLowerCat

from smart_selects.db_fields import ChainedForeignKey

PAYMENT_OPTION_CHOICES = (
    ('cash', 'Payment By Cash'),
    ('bank', 'Payment By Bank'),

)

DEPORT_OPERATION_CHOICES = (
    ('new', 'New Arrival'),
    ('received_from_other_deport', 'Received From Other Deport'),
    ('sales_return', 'Sales Return'),
    ('factory_return', 'Factory Return'),
)


class DeportOperation(models.Model):

    deport_operation = models.CharField(choices=DEPORT_OPERATION_CHOICES,
                                        max_length=30,
                                        help_text='Select Deport Operation: ')
    deport_code = models.ForeignKey(
        Deport, to_field='code', related_name="deport_code")
    date = models.DateTimeField(default=now)

    fundamental_type = models.ForeignKey(FundamentalProductType, blank=True,
                                         null=True)
    # middle_category_type = models.ForeignKey(FPMiddleCat)
    middle_category_type = ChainedForeignKey(
        FPMiddleCat,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
    )
    # lower_category_type = models.ForeignKey(FPLowerCat)
    lower_category_type = ChainedForeignKey(
        FPLowerCat,
        chained_field="middle_category_type",
        chained_model_field="middle_category_type",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True
    )
    # production_item = models.ForeignKey(FinishedProductItem)
    fp_item_chained = ChainedForeignKey(
        FPItem,
        chained_field="lower_category_type",
        chained_model_field="lower_category_type",
        related_name="sale_fp_chained",
        show_all=False,
        auto_choose=True,
        sort=True,
        blank=True,
        null=True,
    )

    fp_item_many = models.ManyToManyField(
        FPItem, blank=True, related_name='sales_fp_many')

    fp_item = models.ForeignKey(FPItem, blank=True, null=True)

    deport_from_code = models.ForeignKey(
        Deport, to_field='code',
        verbose_name="Deport From",
        related_name="deport_from_code",
        blank=True,
        null=True)
    customer = models.ManyToManyField(
        Customer, verbose_name="Customer", blank=True)
    # chalan_no = models.ForeignKey(
    #     Customer, to_field='code', verbose_name="Party")

    def __str__(self):
        return self.deport_operation

    @property
    def get_customer(self):
        return self.customer.first()
    get_customer.fget.short_description = "Customer"


class ExpenseDetail(models.Model):

    date = models.DateTimeField(default=now)
    # serial_no = models.CharField(max_length=100, unique=True)
    # deport_many = models.ManyToManyField(Deport, blank=True, related_name='ed_deport_m')
    deport = models.ManyToManyField(Deport)
    # expense_criteria_many = models.ManyToManyField(
    # ExpenseCriteria, verbose_name="Expense Specification",
    # related_name='ed_exc_m')
    expense_criteria = models.ManyToManyField(
        ExpenseCriteria, verbose_name="Expense Specification")
    # customer_code = models.ForeignKey(Customer, to_field='code')

    detail = models.TextField(blank=True, null=True)
    # payment_option = models.CharField(choices=PAYMENT_OPTION_CHOICES,
    #                                   max_length=30,
    #                                   help_text='Select Payment Option: ')

    invoice_no = models.CharField(max_length=100, unique=True)
    amount = models.IntegerField(default=0)

    def __str__(self):
        # print(self.expense_criteria.first().name)
        return self.get_expense_criteria.name

    @property
    def get_deport(self):
        return self.deport.first()
    get_deport.fget.short_description = "Deport Name"

    @property
    def get_expense_criteria(self):
        return self.expense_criteria.first()
    get_expense_criteria.fget.short_description = "Expense Name"


class Payment(models.Model):

    serial_no = models.CharField(max_length=100, unique=True)
    deport = models.ForeignKey(
        Deport, verbose_name="Deport")
    # deport_code_text = models.CharField(
    #     max_length=100, blank=True, null=True, verbose_name="")

    customer = models.ManyToManyField(
        Customer, verbose_name="Customer")
    date = models.DateTimeField(default=now)
    particular = models.TextField(blank=True, null=True)
    payment_option = models.CharField(choices=PAYMENT_OPTION_CHOICES,
                                      max_length=30,
                                      help_text='Select Payment Option: ')

    transection_no = models.CharField(max_length=100, unique=True)
    amount = models.IntegerField(default=0)

    bank = models.ForeignKey(
        Bank, to_field='code', verbose_name="Select Bank",
        blank=True, null=True)
    # account_no = models.ForeignKey(
    #     BankAccount, to_field='code', verbose_name="A/C No:",
    #     blank=True, null=True)

    # fundamental_type = models.ForeignKey(FundamentalProductType)
    # middle_category_type = models.ForeignKey(FinishedProductItemMiddleCategory)
    account_no = ChainedForeignKey(
        BankAccount,
        chained_field="bank",
        chained_model_field="bank",
        verbose_name="A/C No:",
        blank=True,
        null=True,
        show_all=False,
        auto_choose=True,
        sort=True
    )

    def __str__(self):
        return self.serial_no

    @property
    def get_customer(self):
        return self.customer.first()
    get_customer.fget.short_description = "Customer"


class Sell(models.Model):

    transection_no = models.CharField(max_length=100)
    date = models.DateTimeField(default=now)
    memo_no = models.CharField(max_length=100)
    deport = models.ForeignKey(Deport)
    customer = models.ManyToManyField(Customer)

    grand_total = models.FloatField(
        verbose_name="Grand Total")

    total_commission = models.FloatField(
        verbose_name="Total Commission")
    net_total = models.FloatField(
        verbose_name="Net Total")
    # product_id = models.ForeignKey(FPItem)
    # rate = models.IntegerField(default=0)
    # # product_id = models.ForeignKey(FPItem)
    # # quantity = models.IntegerField(default=1)

    # quantity = models.IntegerField(default=1)
    # commission = models.FloatField(default=1)

    # bank_code = models.ForeignKey(Bank)
    #
    total = models.CharField(max_length=100)

    # @property
    # def grand_total(self):
    #     sell_info = SellDetailInfo.objects.filter(sell=self)
    #     grand_total = 0
    #     for sell in sell_info:
    #         grand_total += sell.total
    #     return grand_total

    # @property
    # def total_commission(self):
    #     return 45

    # @property
    # def net_total(self):
    #     return 66

    total = property(net_total)

    @property
    def get_customer(self):
        return self.customer.first()
    get_customer.fget.short_description = "Customer"

    def __str__(self):
        return self.transection_no


class SellDetailInfo(models.Model):

    sell = models.ForeignKey(Sell)

    product_code = models.ForeignKey(
        FPItem, to_field='code',
        related_name='product_code',
        blank=True,
        null=True,
    )

    product_code_text = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="")

    rate = models.FloatField(default=0)
    quantity = models.FloatField(default=1)

    total = models.FloatField(verbose_name="Total", default=0)

    commission = models.FloatField(default=0)
    net_total = models.FloatField(
        verbose_name="Net Total")

    fundamental_type = models.ForeignKey(
        FundamentalProductType,
        verbose_name='Main Cat', blank=True, null=True)
    # middle_category_type = models.ForeignKey(FPMiddleCat)
    middle_category_type = ChainedForeignKey(
        FPMiddleCat,
        chained_field="fundamental_type",
        chained_model_field="fundamental_type",
        verbose_name="Mid Cat",
        blank=True,
        null=True,
        show_all=False,
        auto_choose=True,
        sort=True
    )
    # lower_category_type = models.ForeignKey(FPLowerCat)
    lower_category_type = ChainedForeignKey(
        FPLowerCat,
        chained_field="middle_category_type",
        chained_model_field="middle_category_type",
        verbose_name="Lower Cat",
        blank=True,
        null=True,
        show_all=False,
        auto_choose=True,
        sort=True
    )
    # production_item = models.ForeignKey(FinishedProductItem)
    finished_product_item = ChainedForeignKey(
        FPItem,
        chained_field="lower_category_type",
        chained_model_field="lower_category_type",
        verbose_name="Product",
        related_name='finished_product_item',
        blank=True,
        null=True,
        show_all=False,
        auto_choose=True,
        sort=True
    )

    # @property
    # def total(self):
    #     return self.rate + self.quantity

    # total = property(total)
    # date = models.DateTimeField(editable=False)

    def save(self, *args, **kw):
        if(self.finished_product_item):
            self.product_code = self.finished_product_item
        # if(self.sell):
        #     self.date = self.sell.date
        super(SellDetailInfo, self).save(*args, **kw)

    def __str__(self):
        return self.sell.transection_no
