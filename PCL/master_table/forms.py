from django import forms
from master_table.models import  FundamentalProductType,\
    RIMiddleCat, RILowerCat, RawItem, FPMiddleCat, FPLowerCat, FPItem



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