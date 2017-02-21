import datetime

from django import forms
from django.forms import ModelForm

# from report.models import FinishedProductReport
from master_table.models import FundamentalProductType,\
    FPMiddleCat, FPLowerCat, FPItem, Shift, RawItem, Customer
from report.models import Report


class ReportForm(forms.ModelForm):

    name = forms.CharField()

    class Meta:
        model = Report
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        # request = kwargs.get('request')
        # print(request)
        if self.data and self.data.get('name') == 'ledger_party':
            self.fields.get('deport').required = True
            self.fields.get('customer').required = True
        elif (self.data and self.data.get('name') == 'ledger_product'):
            self.fields.get('deport').required = True
            self.fields.get('fp_item').required = True
        elif (self.data and self.data.get('name') == 'monthly_party'):
            self.fields.get('deport').required = True
            # self.fields.get('customer').required = True
        elif (self.data and self.data.get('name') == 'monthly_stock'):
            self.fields.get('deport').required = True
        elif (self.data and self.data.get('name') == 'shift_daily_production'):
            self.fields.get('fundamental_type_chained').required = True
            self.fields.get('shift').required = True
        elif (self.data and self.data.get('name') == 'raw_item_stock'):
            self.fields.get('raw_item_report_choices').required = True

        # elif (self.data and self.data.get('name') == 'shift_daily_production'):
        #     self.fields.get('fundamental_type_chained').required = True
        #     self.fields.get('shift').required = True            

        #     print("\n\n.....nothing done")
            # self.data.get('name')

    def clean(self):

        customer = self.cleaned_data.get('customer')
        if(customer and customer.count() > 1):
            raise forms.ValidationError("You can select only one customer")

        deport = self.cleaned_data.get('deport')
        if(deport and customer):
            if(customer.first().deport != deport):
                raise forms.ValidationError(
                    "This customer Does not belong to this deport. Select another customer or another deport")

        if(customer and not deport):
            raise forms.ValidationError(
                "You must select the depot of this customer")

        
        elif (self.cleaned_data.get('name') == 'ledger_product'):
            fp_item = self.cleaned_data.get('fp_item')
            if(fp_item and fp_item.count() > 1):
                raise forms.ValidationError("You can select only one product")

        # select = self.cleaned_data.get('fundamental_type')
        # if(select and select.count() > 1):
        #     raise forms.ValidationError("You can select only one fundamental type")

        # select = self.cleaned_data.get('middle_category_type')
        # if(select and select.count() > 1):
        #     raise forms.ValidationError("You can select only one middle category type")

        # select = self.cleaned_data.get('lower_category_type')
        # if(select and select.count() > 1):
        #     raise forms.ValidationError("You can select only one Lower Category type")

        # select = self.cleaned_data.get('fundamental_type')
        # if(select and select.count() > 1):
        #     raise forms.ValidationError("You can select only one fundamental type")

class SelectionForm(forms.Form):

    start_date = forms.DateField(
        initial=datetime.date.today
    )
    date = datetime.date.today() + datetime.timedelta(-30)
    end_date = forms.DateField(initial=date)
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        help_text="Select Customer",
        # required=False,
    )


class RawItemSelectForm(forms.Form):

    attrs = {"class": "form-control", 'required': 'required'}
    # name = forms.CharField(max_length=50, label='Name',
    #                        widget=forms.TextInput(attrs=attrs))

    rawitem = forms.ModelChoiceField(
        queryset=RawItem.objects.none(),
        label="Select On which on which type you want the report",
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, fundamental_type, *args, **kwargs):

        super(RawItemSelectForm, self).__init__(*args, **kwargs)
        if(fundamental_type):
            self.fields['rawitem'] = forms.MultipleChoiceField(
                widget=forms.CheckboxSelectMultiple, choices=(
                    (s.id, s) for s in RawItem.objects.filter(
                        fundamental_type=fundamental_type)))
        else:
            self.fields['rawitem'] = forms.MultipleChoiceField(
                widget=forms.CheckboxSelectMultiple, choices=(
                    (s.id, s) for s in RawItem.objects.all()))


class ShiftSelectForm(forms.Form):

    attrs = {"class": "form-control", 'required': 'required'}
    # name = forms.CharField(max_length=50, label='Name',
    #                        widget=forms.TextInput(attrs=attrs))

    shift = forms.ModelChoiceField(
        queryset=Shift.objects.none(),
        label="Select On which on which type you want the report",
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, fundamental_type, *args, **kwargs):

        super(ShiftSelectForm, self).__init__(*args, **kwargs)
        if(fundamental_type):
            self.fields['shift'] = forms.MultipleChoiceField(
                widget=forms.CheckboxSelectMultiple, choices=(
                    (s.id, s) for s in Shift.objects.filter(
                        fundamental_type=fundamental_type)))
        else:
            self.fields['shift'] = forms.MultipleChoiceField(
                widget=forms.CheckboxSelectMultiple, choices=(
                    (s.id, s) for s in Shift.objects.all()))


class FundamentalForm(forms.Form):
    attrs = {"class": "form-control", 'required': 'required'}

    fundamental_product_type = forms.ModelChoiceField(
        queryset=FundamentalProductType.objects.all(),
        label="Select On which on which type you want the report",
        # widget=forms.CheckboxSelectMultiple,
    )

    start_date = forms.DateField(initial=datetime.date.today)
    end_date = forms.DateField(initial=datetime.date.today)


class FPBasicForm(forms.Form):
    attrs = {"class": "form-control", 'required': 'required'}
    # name = forms.CharField(max_length=50, label='Name',
    #                        widget=forms.TextInput(attrs=attrs))
    start_date = forms.DateField(initial=datetime.date.today)
    end_date = forms.DateField(initial=datetime.date.today)
    fundamental_product_type = forms.ModelChoiceField(
        queryset=FundamentalProductType.objects.all(),
        label="Select On which on which type you want the report",
        # widget=forms.CheckboxSelectMultiple,
    )
    is_print = forms.BooleanField(initial=False, required=False)


class FPMiddleCatForm(forms.Form):
    attrs = {"class": "form-control", 'required': 'required'}
    fp_middle_cat = forms.ModelChoiceField(
        label="Select Middle Category",
        queryset=FPMiddleCat.objects.none(),
        widget=forms.CheckboxSelectMultiple,
    )
    # start_date = forms.DateField()
    # end_date = forms.DateField()
    is_print = forms.BooleanField(initial=False, required=False)

    def __init__(self, fundamental_type, *args, **kwargs):

        super(FPMiddleCatForm, self).__init__(*args, **kwargs)
        if(fundamental_type):
            self.fields['fp_middle_cat'] = forms.MultipleChoiceField(
                widget=forms.CheckboxSelectMultiple, choices=(
                    (mc.id, mc) for mc in FPMiddleCat.objects.filter(
                        fundamental_type=fundamental_type)))
        else:
            self.fields['fp_middle_cat'] = forms.MultipleChoiceField(
                widget=forms.CheckboxSelectMultiple, choices=(
                    (mc.id, mc) for mc in FPMiddleCat.objects.all()))


class FPLowerCatForm(forms.Form):
    attrs = {"class": "form-control", 'required': 'required'}
    fp_lower_cat = forms.ModelChoiceField(
        label="Select Lower Category",
        queryset=FPLowerCat.objects.none(),
        widget=forms.CheckboxSelectMultiple,
    )
    # start_date = forms.DateField()
    # end_date = forms.DateField()
    is_print = forms.BooleanField(initial=False, required=False)

    def __init__(self, middle_category_type, *args, **kwargs):

        super(FPLowerCatForm, self).__init__(*args, **kwargs)
        if(middle_category_type):
            self.fields['fp_lower_cat'] = forms.MultipleChoiceField(
                widget=forms.CheckboxSelectMultiple, choices=(
                    (lc.id, lc) for lc in FPLowerCat.objects.filter(
                        middle_category_type__in=middle_category_type)))
        else:
            self.fields['fp_lower_cat'] = forms.MultipleChoiceField(
                widget=forms.CheckboxSelectMultiple, choices=(
                    (lc.id, lc) for lc in FPLowerCat.objects.all()))


class FPItemForm(forms.Form):
    attrs = {"class": "form-control", 'required': 'required'}
    fp_item = forms.ModelChoiceField(
        label="Select Finished Item",
        queryset=FPItem.objects.none(),
        widget=forms.CheckboxSelectMultiple,
    )
    # start_date = forms.DateField()
    # end_date = forms.DateField()

    def __init__(self, fp_lower_cat, *args, **kwargs):

        print("\n\n in init method with \n\n")
        # print(fp_lower_cat)
        super(FPItemForm, self).__init__(*args, **kwargs)
        # self.fields['fp_item'].queryset = FinishedProductItem.objects.filter(
        #     lower_category_type__in=fp_lower_cat)
        # self.fields['fp_item'] = forms.MultipleChoiceField(
        # widget=forms.CheckboxSelectMultiple,
        # choices=self.fields['fp_item'].choices)
        if(fp_lower_cat):
            self.fields['fp_item'] = forms.MultipleChoiceField(
                widget=forms.CheckboxSelectMultiple, choices=(
                    (fp.id, fp) for fp in FPItem.objects.filter(
                        lower_category_type__in=fp_lower_cat)))
        else:

            self.fields['fp_item'] = forms.MultipleChoiceField(
                widget=forms.CheckboxSelectMultiple, choices=(
                    (fp.id, fp) for fp in FPItem.objects.all()))


# class FPReportForm(ModelForm):

#     # reading_content = forms.ModelChoiceField(queryset=ReadingContent.objects.all(),
#     #  label="Select Reading Content For This Quick Question",
#     #   widget  = forms.CheckboxSelectMultiple,required=True)

#     middle_cat = forms.ModelChoiceField(
#         queryset=FPMiddleCat.objects.all(),
#         label="Select Middle Category For This Report",
#         widget=forms.CheckboxSelectMultiple, required=False)

#     # excel_file = forms.FileField(required=True )
#     tag = forms.CharField(max_length=100, label="Tag", required=False)
#     # total_question = forms.IntegerField(initial=0, required=True)

#     # marks = forms.IntegerField(initial=1, required=True, label="Individual Question Marks")
#     # negative_marks = forms.IntegerField(initial=25, required=True,
#     #  label="How Percent Marks Will Be Deducted For Wrong Answer: ")

#     # topic_list =
#     # forms.ModelMultipleChoiceField(queryset=ReadingTopic.objects.all(),
#     # widget  = forms.CheckboxSelectMultiple)

#     # profile = forms.ModelChoiceField(queryset=Profile.objects.all(),
#     #         widget=forms.HiddenInput())
#     #
#     class Meta:
#         model = FinishedProductReport
#         # fields = ['name']
#         exclude = []
