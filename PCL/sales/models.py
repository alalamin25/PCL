from django.db import models
from django.utils.timezone import now
from master_table.models import Deport, Customer, FPItem, ExpenseCriteria,\
    Bank, BankAccount

from smart_selects.db_fields import ChainedForeignKey

PAYMENT_OPTION_CHOICES = (
    ('cash', 'Payment By Cash'),
    ('bank', 'Payment By Bank'),

)


class ExpenseDetail(models.Model):

    date = models.DateTimeField(default=now)
    # serial_no = models.CharField(max_length=100, unique=True)
    deport_code = models.ForeignKey(Deport, to_field='code')
    expense_criteria = models.ForeignKey(
        ExpenseCriteria, to_field='code', verbose_name="Expense Specification")
    # customer_code = models.ForeignKey(Customer, to_field='code')

    detail = models.TextField(blank=True, null=True)
    # payment_option = models.CharField(choices=PAYMENT_OPTION_CHOICES,
    #                                   max_length=30,
    #                                   help_text='Select Payment Option: ')

    invoice_no = models.CharField(max_length=100, unique=True)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.expense_criteria.name


class Credit(models.Model):

    serial_no = models.CharField(max_length=100, unique=True)
    deport_code = models.ForeignKey(Deport, to_field='code')
    customer_code = models.ForeignKey(Customer, to_field='code')
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


class Sell(models.Model):

    transection_no = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField(default=now)
    memo_no = models.CharField(max_length=100, unique=True)
    deport_code = models.ForeignKey(Deport, to_field='code')
    # customer_code = models.ForeignKey(Customer, to_field='code')

    # particular = models.TextField(blank=True, null=True)
    # payment_option = models.CharField(choices=PAYMENT_OPTION_CHOICES,
    #                                   max_length=30,
    #                                   help_text='Select Payment Option: ')

    amount = models.IntegerField(default=0)
    # product_id = models.ForeignKey(FPItem)
    # quantity = models.IntegerField(default=1)
    product_id = models.ForeignKey(FPItem)
    quantity = models.IntegerField(default=1)

    # bank_code = models.ForeignKey(Bank)

    def __str__(self):
        return self.serial_no
