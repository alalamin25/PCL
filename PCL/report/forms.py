import datetime

from django import forms
from django.forms import ModelForm

from report.models import FinishedProductReport
from master_table.models import FundamentalProductType,\
    FPMiddleCat, FPLowerCat, FPItem, Shift


class ShiftSelectForm(forms.Form):

    attrs = {"class": "form-control", 'required': 'required'}
    # name = forms.CharField(max_length=50, label='Name',
    #                        widget=forms.TextInput(attrs=attrs))
    start_date = forms.DateField(initial=datetime.date.today)
    end_date = forms.DateField(initial=datetime.date.today)
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
    start_date = forms.DateField()
    end_date = forms.DateField()
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
    start_date = forms.DateField()
    end_date = forms.DateField()
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
    start_date = forms.DateField()
    end_date = forms.DateField()

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


class FPReportForm(ModelForm):

    # reading_content = forms.ModelChoiceField(queryset=ReadingContent.objects.all(),
    #  label="Select Reading Content For This Quick Question",
    #   widget  = forms.CheckboxSelectMultiple,required=True)

    middle_cat = forms.ModelChoiceField(
        queryset=FPMiddleCat.objects.all(),
        label="Select Middle Category For This Report",
        widget=forms.CheckboxSelectMultiple, required=False)

    # excel_file = forms.FileField(required=True )
    tag = forms.CharField(max_length=100, label="Tag", required=False)
    # total_question = forms.IntegerField(initial=0, required=True)

    # marks = forms.IntegerField(initial=1, required=True, label="Individual Question Marks")
    # negative_marks = forms.IntegerField(initial=25, required=True,
    #  label="How Percent Marks Will Be Deducted For Wrong Answer: ")

    # topic_list =
    # forms.ModelMultipleChoiceField(queryset=ReadingTopic.objects.all(),
    # widget  = forms.CheckboxSelectMultiple)

    # profile = forms.ModelChoiceField(queryset=Profile.objects.all(),
    #         widget=forms.HiddenInput())
    #
    class Meta:
        model = FinishedProductReport
        # fields = ['name']
        exclude = []
