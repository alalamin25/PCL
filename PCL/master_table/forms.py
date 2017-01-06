from django import forms
from master_table.models import  FundamentalProductType,\
    RIMiddleCat, RILowerCat, RawItem, FPMiddleCat,\
    FPLowerCat, FPItem, Supplier, Code, Customer, Deport, Bank


class BankForm(forms.ModelForm):

    class Meta:
        model = Bank
        exclude = ()

    def clean(self):

        super(BankForm, self).clean()
        code = self.cleaned_data.get('code')
        base_code = Code.objects.all().first().bank_code
        if(code and base_code):
            full_code = base_code + code.zfill(5)
            if(Bank.objects.filter(code=full_code)):
                raise forms.ValidationError(
                    full_code + ' Has already been taken. Please choose another code')


class DeportForm(forms.ModelForm):

    class Meta:
        model = Deport
        exclude = ()

    def clean(self):

        super(DeportForm, self).clean()
        code = self.cleaned_data.get('code')
        base_code = Code.objects.all().first().deport_code
        if(code and base_code):
            full_code = base_code + code.zfill(5)
            if(Deport.objects.filter(code=full_code)):
                raise forms.ValidationError(
                    full_code + ' Has already been taken. Please choose another code')


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        exclude = ()

    def clean(self):

        super(CustomerForm, self).clean()
        code = self.cleaned_data.get('code')
        base_code = Code.objects.all().first().customer_code
        if(code and base_code):
            full_code = base_code + code.zfill(5)
            if(Customer.objects.filter(code=full_code)):
                raise forms.ValidationError(
                    full_code + ' Has already been taken. Please choose another code')


class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        exclude = ()

    def clean(self):

        super(SupplierForm, self).clean()
        code = self.cleaned_data.get('code')
        base_code = Code.objects.all().first().supplier_code
        if(code and base_code):
            full_code = base_code + code.zfill(5)
            if(Supplier.objects.filter(code=full_code)):
                raise forms.ValidationError(
                    full_code + ' Has already been taken. Please choose another code')


class RawItemForm(forms.ModelForm):

    class Meta:
        model = RawItem
        exclude = ()

    def clean(self):

        super(RawItemForm, self).clean()
        code = self.cleaned_data.get('code')
        lower_category_type = self.cleaned_data.get('lower_category_type')
        if(code and lower_category_type):
            full_code = lower_category_type.code + code.zfill(5)
            if(RawItem.objects.filter(code=full_code)):
                raise forms.ValidationError(
                    full_code + ' Has already been taken. Please choose another code')


class RIMiddleCatForm(forms.ModelForm):

    # code_edit = forms.CharField(max_length=1)

    class Meta:
        model = RIMiddleCat
        exclude = ()

    def clean(self):

        super(RIMiddleCatForm, self).clean()
        # code_edit = self.cleaned_data.get('code_edit')
        code = self.cleaned_data.get('code')
        fundamental_type = self.cleaned_data.get('fundamental_type')
        # self.cleaned_data['code'] = "xs"
        # print(self.cleaned_data.get('code'))
        if(code and fundamental_type):
            full_code = fundamental_type.ri_code + code

            if(RIMiddleCat.objects.filter(code=full_code)):
                raise forms.ValidationError(
                    full_code + ' Has already been taken. Please choose another code')

        return self.cleaned_data


class RILowerCatForm(forms.ModelForm):

    class Meta:
        model = RILowerCat
        exclude = ()

    def clean(self):

        super(RILowerCatForm, self).clean()
        code = self.cleaned_data.get('code')
        # fundamental_type = self.cleaned_data.get('fundamental_type')
        middle_category_type = self.cleaned_data.get('middle_category_type')
        if(code and middle_category_type):
            full_code = middle_category_type.code + code
            if(RILowerCat.objects.filter(code=full_code)):
                raise forms.ValidationError(
                    full_code + ' Has already been taken. Please choose another code')


class FPMiddleCatForm(forms.ModelForm):

    # code_edit = forms.CharField(max_length=1)

    class Meta:
        model = FPMiddleCat
        exclude = ()

    def clean(self):

        super(FPMiddleCatForm, self).clean()
        # code_edit = self.cleaned_data.get('code_edit')
        code = self.cleaned_data.get('code')
        fundamental_type = self.cleaned_data.get('fundamental_type')
        if(code and fundamental_type):
            full_code = fundamental_type.fp_code + code
            if(FPMiddleCat.objects.filter(code=full_code)):
                raise forms.ValidationError(
                    full_code + ' Has already been taken. Please choose another code')


class FPLowerCatForm(forms.ModelForm):

    # code_edit = forms.CharField(max_length=1)

    class Meta:
        model = FPLowerCat
        exclude = ()

    def clean(self):
        # Validation goes here :)
        # fundamental_type = self.cleaned_data.get('fundamental_type')
        # code = fundamental_type.fp_code + form.cleaned_data.get('code_edit')
        super(FPLowerCatForm, self).clean()

        code = self.cleaned_data.get('code')
        fundamental_type = self.cleaned_data.get('fundamental_type')
        middle_category_type = self.cleaned_data.get('middle_category_type')
        if(code and fundamental_type and middle_category_type):
            full_code = middle_category_type.code + code
            if(FPLowerCat.objects.filter(code=full_code)):
                raise forms.ValidationError(
                    full_code + ' Has already been taken. Please choose another code')

# if(code and fundamental_type):
#     full_code = fundamental_type.fp_code + code
#     if(FPMiddleCat.objects.filter(code=full_code)):
#         raise forms.ValidationError(
# full_code + ' Has already been taken. Please choose another code')


class FPItemForm(forms.ModelForm):

    class Meta:
        model = FPItem
        exclude = ()

    def clean(self):

        super(FPItemForm, self).clean()
        code = self.cleaned_data.get('code')
        lower_category_type = self.cleaned_data.get('lower_category_type')
        if(code and lower_category_type):
            full_code = lower_category_type.code + code.zfill(5)
            if(FPItem.objects.filter(code=full_code)):
                raise forms.ValidationError(
                    full_code + ' Has already been taken. Please choose another code')
