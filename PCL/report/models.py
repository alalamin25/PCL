from django.db import models
from django.db.models import Sum
# from django.utils.timezone import now


from smart_selects.db_fields import ChainedManyToManyField
from master_table.models import FundamentalProductType,\
    FPMiddleCat, FPLowerCat, FPItem, Shift, Customer, Deport
from sales.models import DeportOperation, SellDetailInfo


class Report(models.Model):

    start_time = models.DateField()
    end_time = models.DateField()

    deport = models.ForeignKey(Deport, blank=True, null=True)
    customer = models.ManyToManyField(Customer, blank=True)
    fundamental_type = models.ManyToManyField(
        FundamentalProductType, blank=True)
    middle_category_type = models.ManyToManyField(FPMiddleCat, blank=True)
    lower_category_type = models.ManyToManyField(FPLowerCat, blank=True)
    fp_item = models.ManyToManyField(
        FPItem, blank=True, verbose_name="Finished Product")

    @property
    def get_customer(self):
        if(self.customer):
            return self.customer.first()
        return None

    def get_deport_opening_stock(self, fp_item):

        stock = DeportOperation.objects.filter(
            date__date__lt=self.start_time, fp_item=fp_item,
            deport_code=self.deport).aggregate(total=Sum('quantity'))

        if(stock['total']):
            stock = stock['total']
        else:
            stock = 0

        sell = SellDetailInfo.objects.filter(
            sell__date__date__lt=self.start_time, product_code=fp_item,
            sell__deport=self.deport).aggregate(total=Sum('quantity'))
        if(sell['total']):
            sell = sell['total']
        else:
            sell = 0

        val = stock - sell
        return round(val, 2)

    def get_deport_operation(self, fp_item, op_type):

        result = DeportOperation.objects.filter(
            date__date__gte=self.start_time, date__date__lte=self.end_time,
            fp_item=fp_item, deport_operation=op_type,
            deport_code=self.deport).aggregate(total=Sum('quantity'))

        if(result['total']):
            result = result['total']
        else:
            result = 0

        return round(result, 2)

    def get_deport_sell(self, fp_item):

        result = SellDetailInfo.objects.filter(
            sell__date__date__gte=self.start_time, sell__date__date__lte=self.end_time,
            product_code=fp_item,
            sell__deport=self.deport).aggregate(total=Sum('quantity'))

        if(result['total']):
            result = result['total']
        else:
            result = 0

        return round(result, 2)

    def get_deport_to_other(self, fp_item):

        result = DeportOperation.objects.filter(
            date__date__gte=self.start_time, date__date__lte=self.end_time,
            fp_item=fp_item,
            deport_from_code=self.deport).aggregate(total=Sum('quantity'))

        if(result['total']):
            result = result['total']
        else:
            result = 0

        return round(result, 2)
