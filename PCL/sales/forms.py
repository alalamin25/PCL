from django import forms

from sales.models import ExpenseDetail, Payment, DeportOperation, Sell, SellDetailInfo



class SellDetailInfoForm(forms.ModelForm):

    class Meta:
        model = SellDetailInfo
        exclude = ()

    def clean(self):
        # Validation goes here :)
 
        customer = self.cleaned_data.get('customer')
        if(customer and customer.count() > 1):
            raise forms.ValidationError("You can select only one customer")

        deport = self.cleaned_data.get('deport')
        if(deport and customer):
            if(customer.first().deport != deport):
                raise forms.ValidationError(
                    "This customer Does not belong to this deport. Select another customer or another deport")





class SellForm(forms.ModelForm):

    class Meta:
        model = Sell
        exclude = ()

    def clean(self):
        # Validation goes here :)
        customer = self.cleaned_data.get('customer')
        if(customer and customer.count() > 1):
            raise forms.ValidationError("You can select only one customer")

        deport = self.cleaned_data.get('deport')
        if(deport and customer):
            if(customer.first().deport != deport):
                raise forms.ValidationError(
                    "This customer Does not belong to this deport. Select another customer or another deport")





class DeportOperationForm(forms.ModelForm):

    class Meta:
        model = DeportOperation
        exclude = ()


    def __init__(self, *args, **kwargs):
        super(DeportOperationForm, self).__init__(*args, **kwargs)
        # request = kwargs.get('request')
        # print(request)
        if self.data and self.data.get('deport_operation') == 'received_from_other_deport':
            self.fields.get('deport_from_code').required = True
        if self.data and self.data.get('deport_operation') == 'sales_return':
            self.fields.get('customer').required = True
            # self.fields.get('transection_no').required = True
        if self.data and self.data.get('deport_operation') == 'factory_return':
            self.fields.get('deport_from_code').required = True


            # self.fields.get('customer').required = True
        # elif (self.data and self.data.get('name') == 'ledger_product'):
        #     self.fields.get('deport').required = True
        #     self.fields.get('fp_item').required = True
        # elif (self.data and self.data.get('name') == 'monthly_party'):
        #     self.fields.get('deport').required = True
        #     self.fields.get('customer').required = True
        # elif (self.data and self.data.get('name') == 'monthly_stock'):
        #     self.fields.get('deport').required = True



    def clean(self):
        # Validation goes here :)
        customer = self.cleaned_data.get('customer')
        if(customer and customer.count() > 1):
            raise forms.ValidationError("You can select only one customer")

        deport = self.cleaned_data.get('deport_code')
        if(deport and customer):
            if(customer.first().deport != deport):
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
            if(customer.first().deport != deport):
                raise forms.ValidationError(
                    "This customer Does not belong to this deport. Select another customer or another deport")
