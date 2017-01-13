from django import forms

from sales.models import ExpenseDetail, Payment, DeportOperation, Sell



class SellForm(forms.ModelForm):

    class Meta:
        model = Sell
        exclude = ()

    def clean(self):
        # Validation goes here :)
        customer = self.cleaned_data.get('customer')
        if(customer and customer.count() > 1):
            raise forms.ValidationError("You can select only one customer")

        deport = self.cleaned_data.get('deport_code')
        if(deport and customer):
            if(customer.first().deport_code != deport):
                raise forms.ValidationError(
                    "This customer Does not belong to this deport. Select another customer or another deport")





class DeportOperationForm(forms.ModelForm):

    class Meta:
        model = DeportOperation
        exclude = ()

    def clean(self):
        # Validation goes here :)
        customer = self.cleaned_data.get('customer')
        if(customer and customer.count() > 1):
            raise forms.ValidationError("You can select only one customer")

        deport = self.cleaned_data.get('deport_code')
        if(deport and customer):
            if(customer.first().deport_code != deport):
                raise forms.ValidationError(
                    "This customer Does not belong to this deport. Select another customer or another deport")

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
