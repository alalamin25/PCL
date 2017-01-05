from django import forms

from mother_godown.models import PurchaseEntry, IssueEntry


class PurchaseEntryForm(forms.ModelForm):

    class Meta:
        model = PurchaseEntry
        exclude = ()

    def clean(self):
        # Validation goes here :)
        supplier = self.cleaned_data.get('supplier')
        if(supplier and supplier.count() > 1):
            raise forms.ValidationError("You can select only one supplier")

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


class IssueEntryForm(forms.ModelForm):

    class Meta:
        model = IssueEntry
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
