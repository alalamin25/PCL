from django import forms

from sales.models import ExpenseDetail


class ExpenseDetailForm(forms.ModelForm):

    class Meta:
        model = ExpenseDetail
        exclude = ()

    def clean(self):
        # Validation goes here :)
        deport = self.cleaned_data.get('deport')
        if(deport and deport.count() > 1):
            raise forms.ValidationError("You can select only one deport")

        expense_criteria = self.cleaned_data.get('expense_criteria')
        if(expense_criteria and expense_criteria.count() > 1):
            raise forms.ValidationError("You can select only one Expense Criteria")

        # raw_item_chained = self.cleaned_data.get('raw_item_chained')
        # if(expense_criteria and raw_item_chained):
        #     raise forms.ValidationError(
        #         "You can not select Raw Item from two source")

        # if(not(expense_criteria or raw_item_chained)):
        #     raise forms.ValidationError(
        #         "You must select Raw Item from any of two source")