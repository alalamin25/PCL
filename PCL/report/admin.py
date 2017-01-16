from django.contrib import admin
import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now
# from django.core.urlresolvers import reverse

# from report.forms import FPReportForm
from report.models import Report
from report.forms import ReportForm
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
        elif(type == 'monthly_party' ):
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
            return render(request, 'report/sales/ledger_party.html', {})
        elif(type == 'ledger_product'):
            return render(request, 'report/sales/ledger_product.html')
        elif(type == 'monthly_party' ):
            return render(request, 'report/sales/monthly_party.html')
        elif(type == 'monthly_party_gross' ):
            return render(request, 'report/sales/monthly_party_gross.html')
        elif(type == 'monthly_stock' ):
            return render(request, 'report/sales/monthly_stock.html')
        elif(type == 'monthly_stock_gross' ):
            return render(request, 'report/sales/monthly_stock_gross.html')
        print("\n in response post add method")
        return render(request, 'report/sales/report_specification.html', {})


admin.site.register(Report, Report_Admin)
