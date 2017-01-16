from operator import itemgetter
import datetime

from django.contrib import admin
from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now
from django.db.models import Count, Sum, Max
from django.db.models import Value, FloatField

# from report.forms import FPReportForm
from report.models import Report
from sales.models import Payment, Sell, SellDetailInfo
from master_table.models import Customer
from report.forms import ReportForm
from report.util import get_due, get_grand_total, get_total_commission,\
    get_net_total, get_payment
# from report.util import FinishedProductReport_PDF


class Report_Admin(admin.ModelAdmin):

    form = ReportForm
    filter_horizontal = ('customer', 'fundamental_type',
                         'middle_category_type', 'lower_category_type', 'fp_item')

    def save_model(self, request, obj, form, change):
        obj.save()

    def add_view(self, request, extra_context=None):

        extra_context = extra_context or {}
        extra_context['title'] = 'alamin'
        return super(Report_Admin, self).add_view(request, extra_context=extra_context)

    def get_form(self, request, obj=None, **kwargs):

        type = request.GET.get('type')
        form = super(Report_Admin, self).get_form(request, obj, **kwargs)
        if(form.base_fields.get('name')):
            form.base_fields['name'].initial = type
        if(form.base_fields.get('end_time')):
            form.base_fields['end_time'].initial = now()
        date = datetime.date.today() + relativedelta(months=-1)
        if(form.base_fields.get('start_time')):
            form.base_fields['start_time'].initial = date
        # self.initial['memo_no'] = self.transection_no
        #
        # self.exclude = ['name']
        return form

    def get_fields(self, request, obj=None):
        fields = super(Report_Admin, self).get_fields(request, obj)
        # fields.remove('customer')
        type = request.GET.get('type')
        if(type == 'ledger_party'):
            print("\n\n going to remove")
            fields.remove('fundamental_type')
            fields.remove('middle_category_type')
            fields.remove('lower_category_type')
            fields.remove('fp_item')
        elif(type == 'ledger_product'):
            fields.remove('fundamental_type')
            fields.remove('middle_category_type')
            fields.remove('lower_category_type')
            fields.remove('customer')
        elif(type == 'monthly_party'):
            # fields.remove('fundamental_type')
            fields.remove('middle_category_type')
            fields.remove('lower_category_type')
            fields.remove('fp_item')
        elif(type == 'monthly_party_gross'):
            fields.remove('fundamental_type')
            fields.remove('middle_category_type')
            fields.remove('lower_category_type')
            fields.remove('customer')
            fields.remove('fp_item')
        elif(type == 'monthly_stock'):
            fields.remove('fundamental_type')
            fields.remove('middle_category_type')
            fields.remove('lower_category_type')
            fields.remove('customer')
            fields.remove('fp_item')
        elif(type == 'monthly_stock_gross'):
            fields.remove('fundamental_type')
            fields.remove('middle_category_type')
            fields.remove('lower_category_type')
            fields.remove('customer')
            fields.remove('fp_item')
            fields.remove('deport')
        elif(type == 'specification'):
            pass
            # fields.remove('fundamental_type')
            # fields.remove('middle_category_type')
            # fields.remove('lower_category_type')
            # fields.remove('customer')
            # fields.remove('fp_item')
            # fields.remove('deport')

        return fields

    def response_add(self, request, obj, post_url_continue=None):

        type = request.GET.get('type')

        if(type == 'ledger_party'):
            result = []
            print(obj.get_customer)
            payment = Payment.objects.filter(
                customer=obj.get_customer).values()

            sell = Sell.objects.filter(customer=obj.get_customer).values()

            for item in payment:
                item['specification'] = 'Payment'
                result.append(item)
            for item in sell:
                item['specification'] = 'Sale'
                result.append(item)
            result = sorted(result, key=itemgetter('date'))
            print(result)
            print(len(payment))
            opening_due = get_due(
                customer=obj.get_customer, date=obj.start_time)
            closing_due = get_due(
                customer=obj.get_customer, date=obj.end_time+datetime.timedelta(days=1))
            opening_advance = 0
            closing_advance = 0
            if(opening_due < 0):
                opening_advance = -1 * opening_due
                opening_due = 0
            if(closing_due < 0):
                closing_advance = -1 * closing_due
                closing_due = 0

            context = {'result': result,
                       'opening_due': opening_due,
                       'closing_due': closing_due,
                       'opening_advance': opening_advance,
                       'closing_advance': closing_advance,
                       'deport': obj.deport,
                       'customer': obj.get_customer,
                       'start_time': obj.start_time,
                       'end_time': obj.end_time,
                       }

            return render(request, 'report/sales/ledger_party.html', context)

        elif(type == 'specification'):
            result = SellDetailInfo.objects.filter(sell__date__date__gte=obj.start_time,
                                                   sell__date__date__lte=obj.end_time)
            if(obj.deport):
                result = result.filter(sell__deport=obj.deport)

            if(obj.get_customer):
                result = result.filter(sell__customer=obj.get_customer)
            if(obj.fundamental_type.all()):
                result = result.filter(
                    product_code__fundamental_type=obj.fundamental_type.all())
            if(obj.middle_category_type.all()):
                result = result.filter(
                    product_code__middle_category_type=obj.middle_category_type.all())
            if(obj.lower_category_type.all()):
                result = result.filter(
                    product_code__lower_category_type=obj.lower_category_type.all())
            if(obj.fp_item.all()):
                # print(obj.fp_item.all())
                result = result.filter(
                    product_code__in=obj.fp_item.all())

            print(result)
            context = {'result': result,
                       'start_time': obj.start_time,
                       'end_time': obj.end_time,
                       }
            return render(request, 'report/sales/report_specification.html', context)
        elif(type == 'ledger_product'):
            return render(request, 'report/sales/ledger_product.html')

        elif(type == 'monthly_party'):

            result = Sell.objects.filter(date__date__gte=obj.start_time,
                                         date__date__lte=obj.end_time)

            result = Customer.objects.all().values()

            for r in result:
                # r.namee = 'alamin'
                customer = Customer.objects.get(id=r['id'])
                due = get_due(customer, obj.start_time)
                o_due = 0
                o_adv = 0
                if(due > 0):
                    o_due = due
                else:
                    o_adv = -1 * due

                r['opening_due'] = o_due
                r['opening_advance'] = o_adv
                r['grand_total'] = get_grand_total(
                    customer, obj.start_time, obj.end_time)
                r['total_commission'] = get_total_commission(
                    customer, obj.start_time, obj.end_time)
                r['net_total'] = get_net_total(
                    customer, obj.start_time, obj.end_time)
                r['total_due'] = r['opening_due'] + r['net_total']
                r['payment'] = get_payment(
                    customer, obj.start_time, obj.end_time)

                due = get_due(
                    customer, obj.end_time+datetime.timedelta(days=1))
                c_due = 0
                c_adv = 0
                if(due >= 0):
                    c_due = due
                else:
                    c_adv = -1 * due

                r['closing_due'] = c_due
                r['closing_advance'] = c_adv
            # print(result)
            print(len(result))
            # print(result)

            # result = result.values('customer').annotate(
            #     cus_net_total=Sum('net_total'),
            #     cus_total_commission=Sum('total_commission'),
            #     cus_grand_total=Sum('grand_total'),
            #     # due = Sum('net_total') + 10,
            #     total_payment=Sum('payment__amount')

            #     )
            # result = result.extra(select=('due': 'net_total + grand_total'))
            # print(result[0]['customer'])

            # result = result.values('customer').filter(SellDetailInfo)
            # r = result[0]
            # print(r.customer)
            # print(r.payment__set.all())
            # sell = Sell.objects.all().distinct().values('customer')
            # print(sell)
            # # print(sell[0]['customer'])
            # # print(sell[0].customer.all())
            # # print(sell.values())
            # sell = sell.annotate(total_payment=Sum('customer__payment__amount')).distinct().order_by('-date')
            # print(sell.all())
            # sell = set(sell)
            # print(type(sell))
            # sell_list = list(sell)
            # sell_list = set(sell_list)
            # print(sell_list)

            # print(len(sell))

            # print(customer)
            # # print(customer.payment_set.all())
            # customer = customer.annotate(total_payment=Sum('payment__amount'))
            # print(customer.values())
            # print(len(result))
            print(result)
            context = {'result': result,
                       'start_time': obj.start_time,
                       'end_time': obj.end_time,
                       }
            return render(request, 'report/sales/monthly_party.html', context)
        elif(type == 'monthly_party_gross'):
            return render(request, 'report/sales/monthly_party_gross.html')
        elif(type == 'monthly_stock'):
            return render(request, 'report/sales/monthly_stock.html')
        elif(type == 'monthly_stock_gross'):
            return render(request, 'report/sales/monthly_stock_gross.html')
        print("\n in response post add method")
        return render(request, 'report/sales/report_specification.html', {})


admin.site.register(Report, Report_Admin)
