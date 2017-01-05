from django import forms

from production_table.models import RIIssueEntry


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
