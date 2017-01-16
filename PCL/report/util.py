import datetime
from io import BytesIO
from reportlab.pdfgen import canvas

from django.http import HttpResponse
from django.db.models import Count, Sum, Max

from report.models import Report
from sales.models import Payment, Sell, SellDetailInfo
from master_table.models import Customer


def get_grand_total(customer, start_time, end_time):

    expense = Sell.objects.filter(
        customer=customer, date__date__gte=start_time,
        date__date__lte=end_time).aggregate(grand_total=Sum('grand_total'))
    if(expense['grand_total']):
        expense = expense['grand_total']
    else:
        expense = 0
    return round(expense, 2)


def get_total_commission(customer, start_time, end_time):

    expense = Sell.objects.filter(
        customer=customer, date__date__gte=start_time,
        date__date__lte=end_time).aggregate(total_commission=Sum
                                            ('total_commission'))
    if(expense['total_commission']):
        expense = expense['total_commission']
    else:
        expense = 0
    return round(expense, 2)


def get_net_total(customer, start_time, end_time):

    expense = Sell.objects.filter(
        customer=customer, date__date__gte=start_time,
        date__date__lte=end_time).aggregate(net_total=Sum('net_total'))
    if(expense['net_total']):
        expense = expense['net_total']
    else:
        expense = 0
    return round(expense, 2)


def get_payment(customer, start_time, end_time):

    payment = Payment.objects.filter(
        customer=customer, date__date__gte=start_time,
        date__date__lte=end_time).aggregate(amount=Sum('amount'))
    if(payment['amount']):
        payment = payment['amount']
    else:
        payment = 0
    return round(payment, 2)



def get_due(customer, date):

    # print("\n\nin get due method")
    # print(customer)
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

    val = expense - payment
    print(val)
    return round(val, 2)


def FinishedProductReport_PDF(request, file_name='report.pdf'):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=file_name'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "This is a sample report PDF")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


class FPInfo:

    def __init__(self, fp_item):
        self.fp_item = fp_item
        self.unit_amount = 0


class FPResult:

    def __init__(self, date):
        self.date = date
        self.fp_list = []
