from django import forms

from sales.models import ExpenseDetail, Payment, DeportOperation, Sell, SellDetailInfo
from master_table.models import Customer
from report.models import Report


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
        super(SellDetailInfoForm, self).clean()


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

        super(SellForm, self).clean()

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        initial = kwargs.get('initial')
        print("\n\n\n In form init method")
        print(self.fields['deport'].initial)
        print(initial)
        # self.fields['customer'].queryset = Customer.objects.filter(deport=1)
        # self.fields['customer'].choices = [('a','a')]


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
            self.fields.get('chalan_no').required = True
        if self.data and self.data.get('deport_operation') == 'sales_return':
            self.fields.get('customer').required = True
            self.fields.get('memo_no').required = True
            self.fields.get('return_rate').required = True
        if self.data and self.data.get('deport_operation') == 'factory_return':
            self.fields.get('chalan_no').required = True

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

        deport_operation = self.cleaned_data.get('deport_operation')
        if(deport_operation == 'factory_return'):
            deport = self.cleaned_data.get('deport_code')
            fp_item = self.cleaned_data.get('fp_item_many')
            if(not fp_item):
                fp_item = self.cleaned_data.get('fp_item_chained')
            fp_item = fp_item.first()
            quantity = self.cleaned_data.get('quantity')
            date = self.cleaned_data.get('date')
            report = Report(start_time=date, end_time=date,
                                            deport=deport)
            report.save()
            # print("\n\n")
            # print(fp_item)
            # print(type(fp_item))
            report.fp_item.add(fp_item)

            initial_stock = report.get_deport_opening_stock(fp_item=fp_item)

            if(quantity > initial_stock):
                raise forms.ValidationError(
                    "You stock is {} and transection quantity is {}".format(initial_stock, quantity))

        super(DeportOperationForm, self).clean()


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
        super(ExpenseDetailForm, self).clean()


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
        super(PaymentForm, self).clean()
