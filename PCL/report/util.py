import datetime
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse


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
