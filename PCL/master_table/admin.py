from django.contrib import admin
from django.db import models
from django import forms
from django.forms import CheckboxSelectMultiple
from searchableselect.widgets import SearchableSelect

from master_table.models import Supplier, FundamentalProductType,\
    RIMiddleCat, RILowerCat, RawItem, FPMiddleCat, FPLowerCat,\
    ExpenseCriteria, FPItem, Shift, CPItem, CPItemEntry, Deport,\
    Customer, Deport, BankAccount, Bank, Code


class Code_Admin(admin.ModelAdmin):
    pass


class ExpenseCriteria_Admin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_display_links = ('name',)
    search_fields = ('name', 'code')

    fieldsets = [
        (
            'Name Of The Deport: ', {'fields': ['name']}
        ),
        (
            'Unique Code For The Deport: ', {'fields': ['code']}
        ),

    ]


class BankAccount_Admin(admin.ModelAdmin):
    list_display = ('name', 'bank')
    list_display_links = ('name',)
    list_filter = ('bank',)
    search_fields = ('name',)
    raw_id_fields = ('bank', )

    fieldsets = [
        (
            'Select Bank: ', {'fields': ['bank']}
        ),
        (
            'Bank Account No: ', {'fields': ['name']}
        ),
        # (
        #     'Unique Code For Account Number: ', {'fields': ['code']}
        # ),


    ]


class Bank_Admin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_display_links = ('name',)
    search_fields = ('name', 'code')

    fieldsets = [
        (
            'Name Of The Bank: ', {'fields': ['name']}
        ),
        (
            'Unique Code For This Bank: ', {'fields': ['code']}
        ),



    ]


class Deport_Admin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_display_links = ('name',)
    search_fields = ('name', 'code')

    fieldsets = [
        (
            'Name Of The Deport: ', {'fields': ['name']}
        ),
        (
            'Unique Code For The Deport: ', {'fields': ['code']}
        ),

        (
            'Address Of The Deport: ', {'fields': ['address']}
        ),


    ]


class Customer_Admin(admin.ModelAdmin):
    list_display = ('name', 'code', 'deport_code')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('deport_code',)
    raw_id_fields = ('deport_code',)
    fieldsets = [
        (
            'Name Of The Customer: ', {'fields': ['name']}
        ),

        (
            'Unique Code For The Customer: ', {'fields': ['code']}
        ),

        (
            'Select Deport Code: ', {'fields': ['deport_code']}
        ),

        (
            'Address Of The Customer: ', {'fields': ['address']}
        ),

    ]


class FundamentalProductType_Admin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    fieldsets = [
        (
            'Name Of Fundamental Product: ', {'fields': ['name']}
        ),
        (
            'Enter Unique Code: ', {'fields': ['fp_code', 'ri_code']}
        ),
    ]


# class SuplierForm(forms.ModelForm):
#     name5 = forms.CharField()


#     class Meta:
#         model = Suplier
#         exclude = ()
#         widgets = {
#             'Customer': SearchableSelect(model='master_table.Customer', search_field='name', many=False)
#         }


class Supplier_Admin(admin.ModelAdmin):
    # form = SuplierForm
    list_display = ('id', 'name')
    list_display_links = ('id', 'name',)
    list_filter = ()
    search_fields = ('name',)
    # filter_horizontal = ("fundamental_type",)
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    fieldsets = [
        (
            'Name Of The Supplier: ', {'fields': ['name', 'code']}
        ),
        (
            'Select What Type Of Raw Material This Supplier Provides: ', {
                'fields': ['fundamental_type']}
        ),
        (
            'Address Of The Supplier: ', {'fields': ['address']}
        ),
        (
            'Phone Numbers:', {
                'fields': ['phone1', 'phone2', 'phone3', 'phone4', 'phone5']}
        ),
    ]


class RIMiddleCat_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fundamental_type',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('fundamental_type',)
    fieldsets = [
        (
            'Raw Item Middle Category Name: ', {'fields': ['name']}
        ),
        (
            'Choose Fundamental Product Type For This Middle Category Raw Item :', {
                'fields': ['fundamental_type']}
        ),
    ]


class RILowerCat_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fundamental_type', 'middle_category_type')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('fundamental_type', 'middle_category_type',)
    fieldsets = [
        (
            'Raw Material Lower Category Name: ', {'fields': ['name']}
        ),
        (
            'Choose Fundamental Product Type For This Lower Category Raw Item :', {
                'fields': ['fundamental_type']}
        ),
        (
            'Choose Middle Category Type For This Lower Category Raw Item : ', {
                'fields': ['middle_category_type']}
        ),

    ]


class RawItem_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fundamental_type')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('fundamental_type',)
    fieldsets = [
        (
            'Name Of The Raw Material Item: ', {'fields': ['name']}
        ),
        (
            'Choose Fundamental Product Type For This Raw Item:', {
                'fields': ['fundamental_type']}
        ),

        (
            'Choose Middle Category For Raw Item:', {
                'fields': ['middle_category_type']}
        ),
        (
            'Choose Lower Category For Raw Item:', {
                'fields': ['lower_category_type']}
        ),


    ]


class FPMiddleCatForm(forms.ModelForm):

    code_edit = forms.CharField(max_length=1)

    class Meta:
        model = FPMiddleCat
        exclude = ()

    def clean(self):
        # Validation goes here :)
        # fundamental_type = self.cleaned_data.get('fundamental_type')
        # code = fundamental_type.fp_code + form.cleaned_data.get('code_edit')
        super(FPMiddleCatForm, self).clean()
        code_edit = self.cleaned_data.get('code_edit')
        fundamental_type = self.cleaned_data.get('fundamental_type')
        code = fundamental_type.fp_code + code_edit
        if(FPMiddleCat.objects.filter(code=code)):
            raise forms.ValidationError('The Code Must Be Unique')
        # {'password': ["Passwords must be the same."]}


class FPMiddleCat_Admin(admin.ModelAdmin):
    form = FPMiddleCatForm
    list_display = ('id', 'name', 'code', 'fundamental_type',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('fundamental_type',)
    readonly_fields = ('code',)
    fieldsets = [
        (
            'Finished Product Middle Category Name: ', {'fields': ['name']}
        ),
        (
            'Choose Fundamental Product Type For This Middle Category Finished Product:', {
                'fields': ['fundamental_type']}
        ),
        (
            'Unique Code For This Finished Product Middle Category:', {
                'fields': ['code', 'code_edit']}
        ),
        # (
        #     'Write Comment: ', {'fields': ['comment']}
        # ),

    ]

    def save_model(self, request, obj, form, change):
        code_edit = form.cleaned_data.get('code_edit')
        fundamental_type = form.cleaned_data.get('fundamental_type')
        code = fundamental_type.fp_code + code_edit
        obj.code = code
        # print("\n\n code_edit: ")
        # print(code_edit)
        obj.save()


class FPLowerCat_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fundamental_type', 'middle_category_type')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('fundamental_type', 'middle_category_type',)
    fieldsets = [
        (
            'Finished Product Lower Category Name: ', {'fields': ['name']}
        ),
        (
            'Choose Fundamental Product Type For This Lower Category Finished Product :', {
                'fields': ['fundamental_type']}
        ),
        (
            'Choose Middle Category Type For This Lower Category Finished Product: ', {
                'fields': ['middle_category_type']}
        ),
        # (
        #     'Write Comment: ', {'fields': ['comment']}
        # ),

    ]


class FPItem_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'fundamental_type',
                    'middle_category_type', 'lower_category_type')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = (
        'fundamental_type', 'middle_category_type', 'lower_category_type')
    fieldsets = [
        (
            'Name and Of The Production Item: ', {'fields': ['name', 'code']}
        ),
        (
            'Choose Fundamental Product Type For Production Item:', {
                'fields': ['fundamental_type']}
        ),
        (
            'Choose Middle Category For Production Item:', {
                'fields': ['middle_category_type']}
        ),
        (
            'Choose Lower Category For Production Item:', {
                'fields': ['lower_category_type']}
        ),
        (
            'Check Box If This Finished Product Is A Compound Item:', {
                'fields': ['is_cp']}
        ),
        # (
        #     'Write Comment: ', {'fields': ['comment']}
        # ),

    ]


class CPItemEntryInline(admin.TabularInline):
    model = CPItemEntry
    extra = 0


class CPItem_Admin(admin.ModelAdmin):
    list_display = ('id', 'fp_item',)
    list_display_links = ('id', 'fp_item',)
    search_fields = ('fp_item',)
    # list_filter = ('type',)
    # raw_id_fields = ('fp_item', )
    inlines = [CPItemEntryInline]
    fieldsets = [
        (
            'Name Of The Compound Production Item: ', {'fields': ['fp_item']}
        ),

        # (
        #     'Write Comment: ', {'fields': ['comment']}
        # ),

    ]

    def get_form(self, request, obj=None, **kwargs):
        print("\n in get form method")
        form = super(CPItem_Admin, self).get_form(request, obj, **kwargs)
        form.base_fields[
            'fp_item'].queryset = FPItem.objects.filter(is_cp='True')
        return form


class Shift_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fundamental_type', 'start_time', 'end_time')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('fundamental_type', )
    fieldsets = [
        (
            'Name Of The Production Item: ', {'fields': ['name']}
        ),
        (
            'Select Funtamental Product Type ', {
                'fields': ['fundamental_type']}
        ),
        (
            'Select Start Time Of Shift(24 Hours format H:M:S): ', {
                'fields': ['start_time']}
        ),
        (
            'Select End Time Of Shift(24 Hours format H:M:S): ', {
                'fields': ['end_time']}
        ),
        # (
        #     'Write Comment: ', {'fields': ['comment']}
        # ),

    ]


admin.site.register(Supplier, Supplier_Admin)
admin.site.register(FundamentalProductType, FundamentalProductType_Admin)
admin.site.register(RIMiddleCat, RIMiddleCat_Admin)
admin.site.register(RILowerCat, RILowerCat_Admin)
admin.site.register(RawItem, RawItem_Admin)
admin.site.register(FPMiddleCat, FPMiddleCat_Admin)
admin.site.register(FPLowerCat, FPLowerCat_Admin)
admin.site.register(FPItem, FPItem_Admin)
admin.site.register(CPItem, CPItem_Admin)
# admin.site.register(Color, Color_Admin)
admin.site.register(Shift, Shift_Admin)
admin.site.register(Customer, Customer_Admin)
admin.site.register(Deport, Deport_Admin)
admin.site.register(ExpenseCriteria, ExpenseCriteria_Admin)
admin.site.register(Bank, Bank_Admin)
admin.site.register(BankAccount, BankAccount_Admin)
admin.site.register(Code, Code_Admin)
