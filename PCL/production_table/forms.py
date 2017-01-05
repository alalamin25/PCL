from django import forms

from production_table.models import RIIssueEntry, RawItemEntry, RIReturnEntry, ProductionEntry



class ProductionEntryForm(forms.ModelForm):

    class Meta:
        model = ProductionEntry
        exclude = ()

    def clean(self):
        # Validation goes here :)
        fp_item_many = self.cleaned_data.get('fp_item_many')
        if(fp_item_many and fp_item_many.count() > 1):
            raise forms.ValidationError("You can select only one Raw Item")

        fp_item_chained = self.cleaned_data.get('fp_item_chained')
        if(fp_item_many and fp_item_chained):
            raise forms.ValidationError(
                "You can not select Finished Item from two source")

        if(not(fp_item_many or fp_item_chained)):
            raise forms.ValidationError(
                "You must select Finished Item from any of two source")



class RIReturnEntryForm(forms.ModelForm):

    class Meta:
        model = RIReturnEntry
        exclude = ()

    def clean(self):
        # Validation goes here :)
        raw_item_many = self.cleaned_data.get('raw_item_many')
        if(raw_item_many and raw_item_many.count() > 1):
            raise forms.ValidationError("You can select only one Raw Item")

        raw_item_chained = self.cleaned_data.get('raw_item_chained')
        if(raw_item_many and raw_item_chained):
            raise forms.ValidationError(
                "You can not select Raw Item from two source")

        if(not(raw_item_many or raw_item_chained)):
            raise forms.ValidationError(
                "You must select Raw Item from any of two source")



class RIIssueEntryForm(forms.ModelForm):

    class Meta:
        model = RIIssueEntry
        exclude = ()

    def clean(self):
        # Validation goes here :)
        raw_item_many = self.cleaned_data.get('raw_item_many')
        if(raw_item_many and raw_item_many.count() > 1):
            raise forms.ValidationError("You can select only one Raw Item")

        raw_item_chained = self.cleaned_data.get('raw_item_chained')
        if(raw_item_many and raw_item_chained):
            raise forms.ValidationError(
                "You can not select Raw Item from two source")

        if(not(raw_item_many or raw_item_chained)):
            raise forms.ValidationError(
                "You must select Raw Item from any of two source")


class RawItemEntryForm(forms.ModelForm):

    class Meta:
        model = RawItemEntry
        exclude = ()

    def clean(self):
        # Validation goes here :)
        raw_item_many = self.cleaned_data.get('raw_item_many')
        if(raw_item_many and raw_item_many.count() > 1):
            raise forms.ValidationError("You can select only one Raw Item")

        raw_item_chained = self.cleaned_data.get('raw_item_chained')
        if(raw_item_many and raw_item_chained):
            raise forms.ValidationError(
                "You can not select Raw Item from two source")

        if(not(raw_item_many or raw_item_chained)):
            raise forms.ValidationError(
                "You must select Raw Item from any of two source")


