from operator import itemgetter
import datetime

from django.contrib import admin
from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now
from django.db.models import Count, Sum
# from django.core.urlresolvers import reverse

# from report.forms import FPReportForm
from report.models import Report
from sales.models import Payment, Sell
from report.forms import ReportForm
# from report.util import FinishedProductReport_PDF


def get_due(customer, date):
    # print(date)
    expense = Sell.objects.filter(
        customer=customer, date__date__lt=date).aggregate(Sum('net_total'))
    if(expense['net_total__sum']):
        expense = expense['net_total__sum']
    else:
        expense = 0

    payment = Payment.objects.filter(
        customer=customer, date__date__lt=date).aggregate(Sum('amount'))
    if(payment['amount__sum']):
        payment = payment['amount__sum']
    else:
        payment = 0

    print(expense)
    print(payment)

    # return 0
    val = expense - payment
    return round(val, 2)

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
            opening_due = get_due(customer=obj.get_customer, date=obj.start_time)
            closing_due = get_due(customer=obj.get_customer, date=obj.end_time)
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

            }

            return render(request, 'report/sales/ledger_party.html', context)
        elif(type == 'ledger_product'):
            return render(request, 'report/sales/ledger_product.html')
        elif(type == 'monthly_party'):
            return render(request, 'report/sales/monthly_party.html')
        elif(type == 'monthly_party_gross'):
            return render(request, 'report/sales/monthly_party_gross.html')
        elif(type == 'monthly_stock'):
            return render(request, 'report/sales/monthly_stock.html')
        elif(type == 'monthly_stock_gross'):
            return render(request, 'report/sales/monthly_stock_gross.html')
        print("\n in response post add method")
        return render(request, 'report/sales/report_specification.html', {})


admin.site.register(Report, Report_Admin)
