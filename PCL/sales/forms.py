from django import forms

from sales.models import ExpenseDetail, Payment


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
            raise forms.ValidationError(
                "You can select only one Expense Criteria")


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        exclude = ()

    def clean(self):
        # Validation goes here :)
        customer = self.cleaned_data.get('customer')
        if(customer and customer.count() > 1):
            raise forms.ValidationError("You can select only one customer")

        deport = self.cleaned_data.get('deport')
        if(deport and customer):
            if(customer.first().deport_code != deport):
                raise forms.ValidationError(
                    "This customer Does not belong to this deport. Select another customer or another deport")
