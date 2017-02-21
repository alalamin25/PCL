from django.db import models
from django.db.models import Sum, Q
from smart_selects.db_fields import ChainedForeignKey


from smart_selects.db_fields import ChainedManyToManyField
from master_table.models import FundamentalProductType,\
    FPMiddleCat, FPLowerCat, FPItem, Shift, Customer, Deport
from sales.models import DeportOperation, SellDetailInfo


RAW_ITEM_REPORT_CHOICES = (
    ('mother_godown', 'Mother Godown Raw Item Stock Report'),
    ('production_godown', 'Factory Godown Raw Item Stock Report'),
    ('total', 'Total Raw Item Stock Report'),

)


class Report(models.Model):

    # name = models.CharField(max_length=100, editable=False)
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)

    deport = models.ForeignKey(Deport, to_field='code', blank=True, null=True, verbose_name='Depot')
    customer = models.ManyToManyField(Customer, blank=True)
    fundamental_type = models.ManyToManyField(
        FundamentalProductType, blank=True)
    middle_category_type = models.ManyToManyField(FPMiddleCat, blank=True)
    lower_category_type = models.ManyToManyField(FPLowerCat, blank=True)
    fp_item = models.ManyToManyField(
        FPItem, blank=True, verbose_name="Finished Product")

    fundamental_type_chained = models.ForeignKey(FundamentalProductType,
                                                 blank=True, null=True,
                                                 related_name='report_chained',
                                                 verbose_name='Fundamental Type')
    shift = ChainedForeignKey(
        Shift,
        chained_field="fundamental_type_chained",
        chained_model_field="fundamental_type",
        blank=True,
        null=True,
        show_all=False,
        auto_choose=True,
        sort=True
    )
    raw_item_report_choices = models.CharField(choices=RAW_ITEM_REPORT_CHOICES,
                                               max_length=30,
                                               help_text='Select Report Category: ',
                                               blank=True,
                                               null=True)

    @property
    def get_customer(self):
        if(self.customer):
            return self.customer.first()
        return None

    @property
    def get_fp_item(self):
        if(self.fp_item):
            return self.fp_item.first()
        return None

    def get_deport_opening_stock(self, fp_item=None, deport=None):

        if(fp_item):
            stock = DeportOperation.objects.filter(
                date__date__lt=self.start_time, fp_item=fp_item,
                deport_code=self.deport).aggregate(total=Sum('quantity'))
        else:
            stock = DeportOperation.objects.filter(
                date__date__lt=self.start_time,
                deport_code=deport).aggregate(total=Sum('quantity'))
        if(stock['total']):
            stock = stock['total']
        else:
            stock = 0

        if(fp_item):
            sell = SellDetailInfo.objects.filter(
                sell__date__date__lt=self.start_time, product_code=fp_item,
                sell__deport=self.deport).aggregate(total=Sum('quantity'))
        else:
            sell = SellDetailInfo.objects.filter(
                sell__date__date__lt=self.start_time,
                sell__deport=deport).aggregate(total=Sum('quantity'))
        if(sell['total']):
            sell = sell['total']
        else:
            sell = 0

        val = stock - sell
        return round(val, 2)

    def get_deport_operation(self, fp_item=None, deport=None, op_type=None):

        if(fp_item):
            result = DeportOperation.objects.filter(
                date__date__gte=self.start_time, date__date__lte=self.end_time,
                fp_item=fp_item, deport_operation=op_type,
                deport_code=self.deport).aggregate(total=Sum('quantity'))
        else:
            result = DeportOperation.objects.filter(
                date__date__gte=self.start_time, date__date__lte=self.end_time,
                deport_operation=op_type,
                deport_code=deport).aggregate(total=Sum('quantity'))

        if(result['total']):
            result = result['total']
        else:
            result = 0

        return round(result, 2)

    def get_deport_sell(self, fp_item=None, deport=deport):

        if(fp_item):
            result = SellDetailInfo.objects.filter(
                sell__date__date__gte=self.start_time, sell__date__date__lte=self.end_time,
                product_code=fp_item,
                sell__deport=self.deport).aggregate(total=Sum('quantity'))
        else:
            result = SellDetailInfo.objects.filter(
                sell__date__date__gte=self.start_time, sell__date__date__lte=self.end_time,
                sell__deport=deport).aggregate(total=Sum('quantity'))

        if(result['total']):
            result = result['total']
        else:
            result = 0

        return round(result, 2)

    def get_deport_to_other(self, fp_item=None, deport=None):
        if(fp_item):
            result = DeportOperation.objects.filter(
                date__date__gte=self.start_time, date__date__lte=self.end_time,
                fp_item=fp_item,
                deport_from_code=self.deport).aggregate(total=Sum('quantity'))
        else:
            result = DeportOperation.objects.filter(
                date__date__gte=self.start_time, date__date__lte=self.end_time,
                deport_from_code=deport).aggregate(total=Sum('quantity'))

        if(result['total']):
            result = result['total']
        else:
            result = 0

        return round(result, 2)

    def get_deport_gross_total(self, deport=None):

        self.deport = deport
        fp_item = FPItem.objects.all()

        total = 0

        for item in fp_item:
            total_stock = self.get_deport_opening_stock(fp_item=item) +\
                self.get_deport_operation(fp_item=item, op_type='new') +\
                self.get_deport_operation(fp_item=item, op_type='sales_return') +\
                self.get_deport_operation(
                    fp_item=item, op_type='received_from_other_deport')

            total_out = self.get_deport_sell(
                fp_item=item) +\
                self.get_deport_operation(fp_item=item, op_type='factory_return') +\
                self.get_deport_to_other(fp_item=item)

            total_stock = total_stock - total_out
            # if(total_stock < 0):
            #     total_stock = 0

            total += total_stock * item.unit_price
        return round(total, 2)

    def get_deport_product_initial_stock(self):

        incoming = DeportOperation.objects.filter(
            date__date__lt=self.start_time,
            fp_item=self.get_fp_item,
            deport_code=self.deport
        ).aggregate(total_in=Sum('quantity'))['total_in']
        incoming = int(incoming or 0)

        factory_return = DeportOperation.objects.filter(
            date__date__lt=self.start_time,
            fp_item=self.get_fp_item,
            deport_code=self.deport,
            deport_operation='factory_return'

        ).aggregate(total_in=Sum('quantity'))['total_in']
        # print(factory_return)
        factory_return = int(factory_return or 0)

        sell = SellDetailInfo.objects.filter(
            sell__date__date__lt=self.start_time,
            product_code=self.get_fp_item,
            sell__deport=self.deport,
        ).aggregate(total_in=Sum('quantity'))['total_in']
        sell = int(sell or 0)
        # print(incoming)
        # print(factory_return)

        total_in = incoming - factory_return
        total_out = sell + factory_return

        return total_in - total_out
