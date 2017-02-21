from operator import itemgetter
import datetime

from django.contrib import admin
from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now
from django.db.models import Count, Sum, Max, Q
from django.db.models import Value, FloatField

# from report.forms import FPReportForm
from report.models import Report
from sales.models import Payment, Sell, SellDetailInfo, DeportOperation
from master_table.models import Customer, Deport, FPItem
from report.forms import ReportForm
from report.util import get_due, get_grand_total, get_total_commission,\
    get_net_total, get_payment, get_customer_sales_return, get_deport_sales_return
# from report.util import FinishedProductReport_PDF


class Report_Admin(admin.ModelAdmin):

    form = ReportForm
    filter_horizontal = ('customer', 'fundamental_type',
                         'middle_category_type', 'lower_category_type', 'fp_item')
    # exclude = ('name',)
    # readonly_fields=('name',)

    class Media:
        js = ['/static/js/report.js', '/static/sales/js/deport_customer.js']

    def save_model(self, request, obj, form, change):
        obj.save()

    def add_view(self, request, extra_context=None):

        extra_context = extra_context or {}
        extra_context['title'] = 'Report'
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
        fields.remove('shift')
        fields.remove('fundamental_type')
        fields.remove('fundamental_type_chained')
        fields.remove('middle_category_type')
        fields.remove('lower_category_type')
        fields.remove('fp_item')
        fields.remove('customer')
        fields.remove('deport')
        fields.remove('raw_item_report_choices')
        if(type == 'ledger_party'):
            fields.append('deport')
            fields.append('customer')
        elif(type == 'ledger_product'):
            fields.append('deport')
            fields.append('fp_item')
        elif(type == 'monthly_party'):
            # fields.remove('fundamental_type')
            fields.append('deport')
            # fields.append('customer')
            # fields.append('fundamental_type')
        elif(type == 'monthly_party_gross'):
            pass

        elif(type == 'monthly_stock'):
            fields.append('deport')
        elif(type == 'monthly_stock_gross'):
            pass
        elif(type == 'specification'):
            fields.append('deport')
            fields.append('customer')
            fields.append('fundamental_type')
            fields.append('middle_category_type')
            fields.append('lower_category_type')
            fields.append('fp_item')
        elif(type == 'daily_production'):
            fields.remove('end_time')
        elif(type == 'shift_daily_production'):
            fields.remove('end_time')
            fields.append('fundamental_type_chained')
            fields.append('shift')
        elif(type == 'raw_item_stock'):
            fields.append('raw_item_report_choices')

        return fields

    def response_add(self, request, obj, post_url_continue=None):

        type = request.GET.get('type')

        if(type == 'monthly_party'):

            opening_due_total = 0
            opening_advance_total = 0
            grand_total_total = 0
            total_commission_total = 0
            net_total_total = 0
            total_due_total = 0
            payment_total = 0
            sales_return_total = 0
            closing_due_total = 0
            closing_advance_total = 0

            result = Customer.objects.filter(deport=obj.deport).values()
            for r in result:
                # r.namee = 'alamin'
                customer = Customer.objects.get(id=r['id'])
                due = get_due(customer=customer, date=obj.start_time)
                due -= get_customer_sales_return(
                    customer=customer, start_time=obj.start_time, end_time=obj.end_time)
                o_due = 0
                o_adv = 0
                if(due >= 0):
                    o_due = due
                else:
                    o_adv = -1 * due

                r['opening_due'] = o_due
                r['opening_advance'] = o_adv
                r['grand_total'] = get_grand_total(
                    customer=customer, start_time=obj.start_time, end_time=obj.end_time)
                r['total_commission'] = get_total_commission(
                    customer=customer, start_time=obj.start_time, end_time=obj.end_time)
                r['net_total'] = get_net_total(
                    customer=customer, start_time=obj.start_time, end_time=obj.end_time)
                r['total_due'] = r['opening_due'] + r['net_total']
                r['payment'] = get_payment(
                    customer=customer, start_time=obj.start_time, end_time=obj.end_time)

                r['sales_return'] = get_customer_sales_return(customer=customer,
                                                              start_time=obj.start_time,
                                                              end_time=obj.end_time)

                due = get_due(
                    customer=customer, date=obj.end_time+datetime.timedelta(days=1))
                due -= r['sales_return']
                c_due = 0
                c_adv = 0
                if(due >= 0):
                    c_due = due
                else:
                    c_adv = -1 * due
                r['closing_due'] = c_due
                r['closing_advance'] = c_adv

                opening_due_total += r['opening_due']
                opening_advance_total += r['opening_advance']
                grand_total_total += r['grand_total']
                total_commission_total += r['total_commission']
                net_total_total += r['net_total']
                total_due_total += r['total_due']
                payment_total += r['payment']
                sales_return_total += r['sales_return']
                closing_due_total += r['closing_due']
                closing_advance_total += r['closing_advance']

            # print(result)
            # print(len(result))
            # print(result)

            # print(result)
            context = {
                'result': result,
                'deport': obj.deport,
                'start_time': obj.start_time,
                'end_time': obj.end_time,

                'opening_due_total': opening_due_total,
                'opening_advance_total': opening_advance_total,
                'grand_total_total': grand_total_total,
                'total_commission_total': total_commission_total,
                'net_total_total': net_total_total,
                'total_due_total': total_due_total,
                'payment_total': payment_total,
                'sales_return_total': sales_return_total,
                'closing_due_total': closing_due_total,
                'closing_advance_total': closing_advance_total,


            }
            return render(request, 'report/sales/monthly_party.html', context)

        elif(type == 'monthly_party_gross'):

            opening_due_total = 0
            opening_advance_total = 0
            grand_total_total = 0
            total_commission_total = 0
            net_total_total = 0
            total_due_total = 0
            payment_total = 0
            sales_return_total = 0
            closing_due_total = 0
            closing_advance_total = 0

            result = Deport.objects.all().values()
            for r in result:
                # r.namee = 'alamin'
                deport = Deport.objects.get(id=r['id'])
                due = get_due(deport=deport, date=obj.start_time)
                due -= get_deport_sales_return(deport=deport,
                                               start_time=obj.start_time, end_time=obj.end_time)
                o_due = 0
                o_adv = 0
                if(due >= 0):
                    o_due = due
                else:
                    o_adv = -1 * due

                r['opening_due'] = o_due
                r['opening_advance'] = o_adv
                r['grand_total'] = get_grand_total(
                    deport=deport, start_time=obj.start_time,
                    end_time=obj.end_time)
                r['total_commission'] = get_total_commission(
                    deport=deport, start_time=obj.start_time,
                    end_time=obj.end_time)
                r['net_total'] = get_net_total(
                    deport=deport, start_time=obj.start_time,
                    end_time=obj.end_time)
                r['total_due'] = r['opening_due'] + r['net_total']
                r['payment'] = get_payment(
                    deport=deport, start_time=obj.start_time,
                    end_time=obj.end_time)
                r['sales_return'] = get_deport_sales_return(deport=deport,
                                                            start_time=obj.start_time,
                                                            end_time=obj.end_time)
                due = get_due(
                    deport=deport, date=obj.end_time+datetime.timedelta(days=1))
                due = due - r['sales_return']
                c_due = 0
                c_adv = 0
                if(due >= 0):
                    c_due = due
                else:
                    c_adv = -1 * due

                r['closing_due'] = c_due
                r['closing_advance'] = c_adv

                opening_due_total += r['opening_due']
                opening_advance_total += r['opening_advance']
                grand_total_total += r['grand_total']
                total_commission_total += r['total_commission']
                net_total_total += r['net_total']
                total_due_total += r['total_due']
                payment_total += r['payment']
                sales_return_total += r['sales_return']
                closing_due_total += r['closing_due']
                closing_advance_total += r['closing_advance']

            # print(result)

            context = {
                'result': result,
                'start_time': obj.start_time,
                'end_time': obj.end_time,
                'opening_due_total': opening_due_total,
                'opening_advance_total': opening_advance_total,
                'grand_total_total': grand_total_total,
                'total_commission_total': total_commission_total,
                'net_total_total': net_total_total,
                'total_due_total': total_due_total,
                'payment_total': payment_total,
                'sales_return_total': sales_return_total,
                'closing_due_total': closing_due_total,
                'closing_advance_total': closing_advance_total,



            }
            return render(request, 'report/sales/monthly_party_gross.html', context)

        elif(type == 'monthly_stock'):

            result = FPItem.objects.all().distinct().values()

            # result = FPItem.objects.filter(Q(deportoperation__deport_code=obj.deport) | Q(deportoperation__deport_from_code=obj.deport)).distinct().values()
            for r in result:
                # print(r)
                fp_item = FPItem.objects.get(id=r['id'])
                # print(fp_item)
                r['opening_stock'] = obj.get_deport_opening_stock(
                    fp_item=fp_item)
                r['new'] = obj.get_deport_operation(
                    fp_item=fp_item, op_type='new')
                r['received_from_other_deport'] = obj.get_deport_operation(
                    fp_item=fp_item,
                    op_type='received_from_other_deport')

                # r['received_from_other_deport'] = obj.get_deport_operation(
                #     fp_item,
                #     op_type='received_from_other_deport')
                r['sales_return'] = obj.get_deport_operation(
                    fp_item=fp_item,
                    op_type='sales_return')
                r['total_stock'] = r['opening_stock'] + r['new'] +\
                    r['received_from_other_deport'] + r['sales_return']

                r['sell'] = obj.get_deport_sell(fp_item=fp_item)
                r['factory_return'] = obj.get_deport_operation(
                    fp_item=fp_item,
                    op_type='factory_return')
                r['return_to_other_deport'] = obj.get_deport_to_other(
                    fp_item=fp_item)
                r['total_outgoing'] = r['sell'] + \
                    r['factory_return'] + r['return_to_other_deport']
                r['closing_stock'] = r['total_stock'] - r['total_outgoing']
                r['gross_total'] = r['closing_stock'] * r['unit_price']
            # print(result)

            context = {'result': result,
                       'start_time': obj.start_time,
                       'end_time': obj.end_time,
                       'deport': obj.deport,
                       }
            deport = obj.deport
            context['opening_stock_total'] = obj.get_deport_opening_stock(
                deport=deport)
            context['new_total'] = obj.get_deport_operation(
                deport=deport, op_type='new')
            context['received_from_other_deport_total'] = obj.get_deport_operation(
                deport=deport,
                op_type='received_from_other_deport')

            # context['received_from_other_deport'] = obj.get_deport_operation(
            #     deport,
            #     op_type='received_from_other_deport')
            context['sales_return_total'] = obj.get_deport_operation(
                deport=deport,
                op_type='sales_return')
            context['total_stock_total'] = context['opening_stock_total'] + context['new_total'] +\
                context['received_from_other_deport_total'] + \
                context['sales_return_total']

            context['sell_total'] = obj.get_deport_sell(deport=deport)
            context['factory_return_total'] = obj.get_deport_operation(
                deport=deport,
                op_type='factory_return')
            context['return_to_other_deport_total'] = obj.get_deport_to_other(
                deport=deport)
            context['total_outgoing_total'] = context['sell_total'] + \
                context['factory_return_total'] + \
                context['return_to_other_deport_total']

            context['closing_stock_total'] = context[
                'total_stock_total'] - context['total_outgoing_total']
            context['gross_total_total'] = obj.get_deport_gross_total(
                deport=deport)

            return render(request, 'report/sales/monthly_stock.html', context)

        elif(type == 'monthly_stock_gross'):

            opening_stock_total = 0
            new_total = 0
            received_from_other_deport_total = 0
            sales_return_total = 0
            total_stock_total = 0
            sell_total = 0
            factory_return_total = 0
            return_to_other_deport_total = 0
            total_outgoing_total = 0
            closing_stock_total = 0
            gross_total_total = 0

            result = Deport.objects.all().distinct().values()
            for r in result:
                # print(r)
                deport = Deport.objects.get(id=r['id'])
                # print(fp_item)
                r['opening_stock'] = obj.get_deport_opening_stock(
                    deport=deport)
                r['new'] = obj.get_deport_operation(
                    deport=deport, op_type='new')
                r['received_from_other_deport'] = obj.get_deport_operation(
                    deport=deport,
                    op_type='received_from_other_deport')

                # r['received_from_other_deport'] = obj.get_deport_operation(
                #     deport,
                #     op_type='received_from_other_deport')
                r['sales_return'] = obj.get_deport_operation(
                    deport=deport,
                    op_type='sales_return')
                r['total_stock'] = r['opening_stock'] + r['new'] +\
                    r['received_from_other_deport'] + r['sales_return']

                r['sell'] = obj.get_deport_sell(deport=deport)
                r['factory_return'] = obj.get_deport_operation(
                    deport=deport,
                    op_type='factory_return')
                r['return_to_other_deport'] = obj.get_deport_to_other(
                    deport=deport)
                r['total_outgoing'] = r['sell'] + \
                    r['factory_return'] + r['return_to_other_deport']
                r['closing_stock'] = r['total_stock'] - r['total_outgoing']
                r['gross_total'] = obj.get_deport_gross_total(deport=deport)

                opening_stock_total += r['opening_stock']
                new_total += r['new']
                received_from_other_deport_total += r['received_from_other_deport']
                sales_return_total += r['sales_return']
                total_stock_total += r['total_stock']
                sell_total += r['sell']
                factory_return_total += r['factory_return']
                return_to_other_deport_total += r['return_to_other_deport']
                total_outgoing_total += r['total_outgoing']
                closing_stock_total += r['closing_stock']
                gross_total_total += r['gross_total']

            # print(result)

            context = {'result': result,
                       'start_time': obj.start_time,
                       'end_time': obj.end_time,
                       'opening_stock_total': opening_stock_total,
                       'new_total': new_total,
                       'received_from_other_deport_total': received_from_other_deport_total,
                       'sales_return_total': sales_return_total,
                       'total_stock_total': total_stock_total,
                       'sell_total': sell_total,
                       'factory_return_total': factory_return_total,
                       'return_to_other_deport_total': return_to_other_deport_total,
                       'total_outgoing_total': total_outgoing_total,
                       'closing_stock_total': closing_stock_total,
                       'gross_total_total': gross_total_total,
                       }

            return render(request, 'report/sales/monthly_stock_gross.html', context)

        elif(type == 'ledger_party'):
            result = []
            # print(obj.get_customer)
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
            # print(result)
            # print(len(payment))
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

        elif(type == 'ledger_product'):

            result = DeportOperation.objects.filter(
                date__date__gte=obj.start_time,
                date__date__lte=obj.end_time,
                fp_item=obj.get_fp_item,
                deport_code=obj.deport
            ).values()

            final_result = []
            for r in result:
                if(r['deport_operation'] == 'new'):
                    r['specification'] = 'New Arrival'
                    r['in'] = r['quantity']
                elif(r['deport_operation'] == 'received_from_other_deport'):
                    r['specification'] = 'Received From Other Deport'
                    r['in'] = r['quantity']
                elif(r['deport_operation'] == 'sales_return'):
                    r['specification'] = 'Sales Return'
                    r['in'] = r['quantity']
                elif(r['deport_operation'] == 'factory_return'):
                    r['specification'] = 'Factory Return'
                    r['out'] = r['quantity']

                final_result.append(r)

            # final_result = list(result)

            result = SellDetailInfo.objects.filter(
                sell__date__date__gte=obj.start_time,
                sell__date__date__lte=obj.end_time,
                product_code=obj.get_fp_item,
                sell__deport=obj.deport,
            ).values('sell__date', 'quantity')

            for r in result:
                r['date'] = r['sell__date']
                r['specification'] = 'Sale'
                r['out'] = r['quantity']
                final_result.append(r)
                # print(r)

            result = final_result
            in_total = 0
            out_total = 0
            for r in result:
                if(r.get('in')):
                    in_total += r['in']
                elif(r.get('out')):
                    out_total += r['out']
            opening_stock = obj.get_deport_product_initial_stock()
            closing_stock = opening_stock + in_total - out_total
            value = obj.get_fp_item.unit_price * closing_stock

            context = {
                'result': result,
                'deport': obj.deport,
                'fp_item': obj.get_fp_item,
                'start_time': obj.start_time,
                'end_time': obj.end_time,
                'in_total': in_total,
                'out_total': out_total,
                'opening_stock': opening_stock,
                'closing_stock': closing_stock,
                'value':  value,
            }
            return render(request, 'report/sales/ledger_product.html', context)

        elif(type == 'specification'):

            result = SellDetailInfo.objects.filter(sell__date__date__gte=obj.start_time,
                                                   sell__date__date__lte=obj.end_time)
            if(obj.deport):
                result = result.filter(sell__deport=obj.deport)

            if(obj.get_customer):
                result = result.filter(sell__customer=obj.get_customer)
            if(obj.fundamental_type.all()):
                result = result.filter(
                    product_code__fundamental_type__in=obj.fundamental_type.all())
            if(obj.middle_category_type.all()):
                result = result.filter(
                    product_code__middle_category_type__in=obj.middle_category_type.all())
            if(obj.lower_category_type.all()):
                result = result.filter(
                    product_code__lower_category_type__in=obj.lower_category_type.all())
            if(obj.fp_item.all()):
                # print(obj.fp_item.all())
                result = result.filter(
                    product_code__in=obj.fp_item.all())

            print(result)
            total_total = 0
            commission_total = 0
            net_total_total = 0
            for r in result:
                total_total += r.total
                net_total_total += r.net_total
                commission_total += r.total - r.net_total

            context = {'result': result,
                       'start_time': obj.start_time,
                       'end_time': obj.end_time,
                       'total_total': total_total,
                       'net_total_total': net_total_total,
                       'commission_total': commission_total,
                       }
            return render(request, 'report/sales/report_specification.html', context)

        elif(type == 'daily_production'):

            result = ""

            context = {'result': result,
                       'start_time': obj.start_time,
                       # 'end_time': obj.end_time,
                       }

            return render(request, 'report/others/daily_production.html', context)

        elif(type == 'shift_daily_production'):

            result = ""

            context = {'result': result,
                       'start_time': obj.start_time,
                       'shift': obj.shift
                       }

            return render(request, 'report/others/shift_daily_production.html', context)

        elif(type == 'raw_item_purchase'):

            result = ""

            context = {'result': result,
                       'start_time': obj.start_time,
                       'end_time': obj.end_time,
                       'shift': obj.shift
                       }

            return render(request, 'report/others/ri_purchase.html', context)

        elif(type == 'raw_item_stock'):

            result = ""

            if(obj.raw_item_report_choices == 'mother_godown'):
                context = {'result': result,
                           'start_time': obj.start_time,
                           'shift': obj.shift
                           }

                return render(request, 'report/others/ri_stock_mother_godown.html', context)

            if(obj.raw_item_report_choices == 'production_godown'):
                context = {'result': result,
                           'start_time': obj.start_time,
                           'shift': obj.shift
                           }

                return render(request, 'report/others/ri_stock_production_godown.html', context)

            if(obj.raw_item_report_choices == 'total'):
                context = {'result': result,
                           'start_time': obj.start_time,
                           'shift': obj.shift
                           }

                return render(request, 'report/others/ri_stock_total.html', context)

        print("\n in response post add method")
        return render(request, 'report/sales/report_specification.html', {})


admin.site.register(Report, Report_Admin)
