from io import BytesIO
from datetime import timedelta
from reportlab.pdfgen import canvas


from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.db.models import Sum

from django.template import Context
from django.template.loader import get_template
# from xhtml2pdf import pisa
# from easy_pdf.views import PDFTemplateView
import pdfkit

from report.forms import FPBasicForm, FPMiddleCatForm, FPLowerCatForm, FPItemForm
from master_table.models import FundamentalProductType, FPMiddleCat, FPLowerCat,\
    FinishedProductItem
from production_table.models import ProductionEntry

from report.util import FPResult, FPInfo


class IndexView(TemplateView):
    template_name = "report/home.html"


class FpReportView(View):
    fp_basic_form = FPBasicForm
    template_name = 'report/fp_report.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name,
                      {'form': self.fp_basic_form})

    def post(self, request, *args, **kwargs):
        pass


class FpMiddleCatView(View):
    fp_basic_form = FPBasicForm
    template_name = 'report/fp_mid_cat.html'

    # def get(self, request, *args, **kwargs):
    #     # form = self.form_class(initial=self.initial)
    # return render(request, self.template_name, {'form': self.fp_basic_form})

    def get(self, request, *args, **kwargs):
        print("\n in class view")
        # form = FPMiddleCatForm
        fp_basic_form = self.fp_basic_form(request.GET)
        if fp_basic_form.is_valid():
            print("The FPbasic form is valid")
            fundamental_type = fp_basic_form.cleaned_data[
                'fundamental_product_type']
            form = FPMiddleCatForm()
            form.fields['start_date'].initial = fp_basic_form.cleaned_data[
                'start_date']
            form.fields['end_date'].initial = fp_basic_form.cleaned_data[
                'end_date']
            form.fields['fp_middle_cat'].queryset = FPMiddleCat.objects.filter(
                fundamental_type=fundamental_type)
            return render(request, self.template_name, {'form': form})
        else:
            print("The basic form is not valid")
            print(fp_basic_form.errors)
            return redirect(reverse('fp_report'))

        # return render(request, self.template_name, {'form': form})


class FpLowerCatView(View):
    fp = FPMiddleCatForm
    template_name = 'report/fp_lower_cat.html'

    def get(self, request, *args, **kwargs):
        print("lower cat class view get method\n")

        fp_middle_cat_form = self.fp(request.GET)
        if(fp_middle_cat_form):
            print("The form is not none type\n\n\n")
            print(self.fp)
            # print(fp_middle_cat_form)
        fp_middle_cat = request.GET.getlist('fp_middle_cat')
        if fp_middle_cat:
            print("The FPMiddle cat form is valid")
            # fp_middle_cat = fp_middle_cat_form.cleaned_data[
            #     'fp_middle_cat']
            form = FPLowerCatForm()
            form.fields['start_date'].initial = request.GET.get('start_date')
            form.fields['end_date'].initial = request.GET.get('end_date')
            print(type(fp_middle_cat))
            print(fp_middle_cat)
            form.fields['fp_lower_cat'].queryset = FPLowerCat.objects.filter(
                middle_category_type__in=fp_middle_cat)
            return render(request, self.template_name, {'form': form})
        else:
            print("The middle cat form is not valid")
            print(fp_middle_cat_form.errors)
            return redirect(reverse('fp_report'))


class FpItemView(View):
    fp = FPMiddleCatForm
    template_name = 'report/fp_item.html'

    def get(self, request, *args, **kwargs):
        # print("lower cat class view get method\n")

        fp_lower_cat = request.GET.getlist('fp_lower_cat')
        if fp_lower_cat:

            form = FPItemForm(fp_lower_cat)
            # form = FPItemForm(fp_lower_cat)
            form.fields['start_date'].initial = request.GET.get('start_date')
            form.fields['end_date'].initial = request.GET.get('end_date')

            form.fields['fp_item'].queryset = FinishedProductItem.objects.filter(
                lower_category_type__in=fp_lower_cat)
            # form.fields['fp_item'].widget.choices = FinishedProductItem.objects.filter(
            #     lower_category_type__in=fp_lower_cat).choices
            return render(request, self.template_name, {'form': form})
        else:
            print("The middle cat form is not valid")
            print(fp_middle_cat_form.errorsss)
            return redirect(reverse('fp_report'))


class FpItemReportView(View):
    template_name = 'report/fp_item_report.html'
    fp_item_form = FPItemForm

    def get(self, request, *args, **kwargs):
        return HttpResponse("In get method")

    def returnPdf(self, context):

        template = get_template(self.template_name)
        html = template.render(Context(context))
        # print(html)
        pdf = pdfkit.from_string(html, False)

        # pdf = pdfkit.from_url('http://ourcodeworld.com', False)
        response = HttpResponse(pdf, content_type='application/pdf')
        response[
            'Content-Disposition'] = 'attachment; filename="ourcodeworld.pdf"'

        return response

    def getListOfDates(self, start_date, end_date):
        date_list = []
        day_count = (end_date - start_date).days + 1
        for n in range(day_count):
            new_date = start_date + timedelta(n)
            # print(new_date)
            date_list.append(new_date)
        return date_list

    def getFPSearchResult(self, date_list, fp_item):
        print("fp_search_result page")
        print(fp_item)
        fp_search_result = []
        print(fp_search_result)

        print("Deleting fp_search sesurlt")

        for date in date_list:
            fp_result = FPResult(date)
            for fp in fp_item:
                result = ProductionEntry.objects.filter(
                    creation_time__year=date.year,
                    creation_time__month=date.month,
                    creation_time__day=date.day,
                    finished_product_item=fp).aggregate(Sum('unit_amount'))
                # print(
                # "The result of {0} and typeof fp {1}is {2}".format(fp, " ", result))
                if(result['unit_amount__sum']):
                    print(
                        "\n\n\n\nThe result of {0} is {1}\n\n\n".format(fp, result))
                    fp_info = FPInfo(fp)
                    fp_info.unit_amount = result['unit_amount__sum']
                    fp_result.fp_list.append(fp_info)
            if(len(fp_result.fp_list) > 0):
                print("........ appending to fpsearch result........")
                fp_search_result.append(fp_result)

        print("\n returning\n")
        print(fp_search_result)
        return fp_search_result

    def post(self, request, *args, **kwargs):

        context = {}

        # fp_item_form = FPItemForm(request.POST)
        fp_item_form = FPItemForm("", request.POST)

        if(fp_item_form.is_valid()):
            fp_item = fp_item_form.cleaned_data['fp_item']
            fp_item = FinishedProductItem.objects.filter(id__in=fp_item)
            context['fp_item'] = fp_item
            start_date = fp_item_form.cleaned_data['start_date']
            end_date = fp_item_form.cleaned_data['end_date']
            date_list = self.getListOfDates(start_date, end_date)

            context['date_list'] = date_list
            fp_search_result = self.getFPSearchResult(date_list, fp_item)
            print(fp_search_result)
            context['fp_search_result'] = fp_search_result

            # return self.returnPdf(context)
            print(context)
            return render(request, self.template_name, context)
        else:
            print(fp_item_form.errors)
            return HttpResponse("The form is invalid")
