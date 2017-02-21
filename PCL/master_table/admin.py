from django.contrib import admin
from django.db import models
from django import forms
from django.forms import CheckboxSelectMultiple
from searchableselect.widgets import SearchableSelect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from master_table.models import Supplier, FundamentalProductType,\
    RIMiddleCat, RILowerCat, RawItem, FPMiddleCat, FPLowerCat,\
    ExpenseCriteria, FPItem, Shift, CPItem, CPItemEntry, Deport,\
    Customer, Deport, BankAccount, Bank, Code

from master_table.forms import FPMiddleCatForm, FPLowerCatForm, FPItemForm,\
    RIMiddleCatForm, RILowerCatForm, RawItemForm, SupplierForm, CustomerForm, DeportForm, BankForm


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

    form = BankForm
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

    def get_readonly_fields(self, request, obj=None):
        # This is the case when obj is already created i.e. it's an edit
        if obj:
            return ['code']
        else:
            return []

    def save_model(self, request, obj, form, change):

        base_code = Code.objects.all().first().bank_code
        if(not obj.id):
            if(obj.code):
                code = base_code + (obj.code).zfill(5)
                obj.code = code
            else:
                for i in range(1, 99999, 1):
                    temp = str(i).zfill(5)
                    temp_code = base_code + temp
                    if(Bank.objects.filter(code=temp_code)):
                        continue
                    obj.code = temp_code
                    break

        obj.save()

    def response_change(self, request, obj, post_url_continue=None):
        print("\n in response post add method")
        return HttpResponse("/dsaf")


class Deport_Admin(admin.ModelAdmin):

    form = DeportForm
    list_display = ('id', 'name', 'code')
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

    def get_readonly_fields(self, request, obj=None):
        # This is the case when obj is already created i.e. it's an edit
        if obj:
            return ['code']
        else:
            return []

    def save_model(self, request, obj, form, change):

        base_code = Code.objects.all().first().deport_code
        if(not obj.id):
            if(obj.code):
                code = base_code + (obj.code).zfill(5)
                obj.code = code
            else:
                for i in range(1, 99999, 1):
                    temp = str(i).zfill(5)
                    temp_code = base_code + temp
                    if(Deport.objects.filter(code=temp_code)):
                        continue
                    obj.code = temp_code
                    break

        obj.save()


class Customer_Admin(admin.ModelAdmin):

    form = CustomerForm
    list_display = ('name', 'code', 'deport')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('deport',)
    # raw_id_fields = ('deport',)
    fieldsets = [
        (
            'Name Of The Customer: ', {'fields': ['name']}
        ),

        (
            'Unique Code(5 digit number) For The Customer(If blank then automatically be added): ', {'fields': ['code']}
        ),

        (
            'Select Deport Code: ', {'fields': ['deport']}
        ),

        (
            'Address Of The Customer: ', {'fields': ['address']}
        ),

    ]

    def get_readonly_fields(self, request, obj=None):
        # This is the case when obj is already created i.e. it's an edit
        if obj:
            return ['code']
        else:
            return []

    def save_model(self, request, obj, form, change):

        base_code = Code.objects.all().first().customer_code
        if(not obj.id):
            if(obj.code):
                code = base_code + (obj.code).zfill(5)
                obj.code = code
            else:
                for i in range(1, 99999, 1):
                    temp = str(i).zfill(5)
                    temp_code = base_code + temp
                    if(Customer.objects.filter(code=temp_code)):
                        continue
                    obj.code = temp_code
                    break

        obj.save()


class FundamentalProductType_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fp_code', 'ri_code')
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

    def get_readonly_fields(self, request, obj=None):
        # This is the case when obj is already created i.e. it's an edit
        if obj:
            return ['fp_code', 'ri_code']
        else:
            return []


# class SuplierForm(forms.ModelForm):
#     name5 = forms.CharField()


#     class Meta:
#         model = Suplier
#         exclude = ()
#         widgets = {
#             'Customer': SearchableSelect(model='master_table.Customer', search_field='name', many=False)
#         }


class Supplier_Admin(admin.ModelAdmin):

    form = SupplierForm
    list_display = ('id', 'name', 'code')
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

    def get_readonly_fields(self, request, obj=None):
        # This is the case when obj is already created i.e. it's an edit
        if obj:
            return ['code']
        else:
            return []

    def save_model(self, request, obj, form, change):

        base_code = Code.objects.all().first().supplier_code
        if(not obj.id):
            if(obj.code):
                code = base_code + (obj.code).zfill(5)
                obj.code = code
            else:
                for i in range(1, 99999, 1):
                    temp = str(i).zfill(5)
                    temp_code = base_code + temp
                    if(Supplier.objects.filter(code=temp_code)):
                        continue
                    obj.code = temp_code
                    break

        obj.save()


class RIMiddleCat_Admin(admin.ModelAdmin):
    form = RIMiddleCatForm
    list_display = ('id', 'name', 'code', 'fundamental_type',)
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

        (
            'Unique Code For This Finished Product Middle Category:', {
                'fields': ['code']}
        ),
    ]

    def get_readonly_fields(self, request, obj=None):
        # This is the case when obj is already created i.e. it's an edit
        if obj:
            return ['code', 'fundamental_type']
        else:
            return []

    def save_model(self, request, obj, form, change):

        if(not obj.id):
            code = obj.fundamental_type.ri_code + obj.code
            obj.code = code
        obj.save()


class RILowerCat_Admin(admin.ModelAdmin):
    form = RILowerCatForm
    list_display = (
        'id', 'name', 'code', 'fundamental_type', 'middle_category_type')
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

        (
            'Unique Code For This Finished Product Middle Category:', {
                'fields': ['code']}
        ),

    ]

    def get_readonly_fields(self, request, obj=None):
        # This is the case when obj is already created i.e. it's an edit
        if obj:
            return ['code', 'fundamental_type', 'middle_category_type']
        else:
            return []

    def save_model(self, request, obj, form, change):

        if(not obj.id):
            code = obj.middle_category_type.code + obj.code
            obj.code = code
        obj.save()


class RawItem_Admin(admin.ModelAdmin):
    form = RawItemForm
    list_display = ('id', 'name', 'code', 'fundamental_type')
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

        (
            'Unique Code For This Finished Product Middle Category:', {
                'fields': ['code']}
        ),
        (
            'Optional Grade Field For Raw Item:', {
                'fields': ['grade']}
        ),

    ]

    def get_readonly_fields(self, request, obj=None):
        # This is the case when obj is already created i.e. it's an edit
        if obj:
            return ['code', 'fundamental_type', 'middle_category_type', 'lower_category_type']
        else:
            return []

    def save_model(self, request, obj, form, change):

        if(not obj.id):
            if(obj.code):
                code = obj.lower_category_type.code + (obj.code).zfill(5)
                obj.code = code
            else:
                for i in range(1, 99999, 1):
                    temp = str(i).zfill(5)
                    temp_code = obj.lower_category_type.code + temp
                    if(RawItem.objects.filter(code=temp_code)):
                        continue
                    obj.code = temp_code
                    break

        obj.save()


class FPMiddleCat_Admin(admin.ModelAdmin):
    form = FPMiddleCatForm
    list_display = ('id', 'name', 'code', 'fundamental_type',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('fundamental_type',)
    # readonly_fields = ('code',)
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
                'fields': ['code']}
        ),

    ]

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(FPMiddleCat_Admin, self).get_form(request, obj, **kwargs)
    #     # code = obj.code
    #     # form.base_fields['code_edit'].initial = code
    #     return form

    def get_readonly_fields(self, request, obj=None):
        # This is the case when obj is already created i.e. it's an edit
        if obj:
            return ['code', 'fundamental_type']
        else:
            return []

    def save_model(self, request, obj, form, change):
        # code = form.cleaned_data.get('code')
        # fundamental_type = form.cleaned_data.get('fundamental_type')
        if(not obj.id):
            code = obj.fundamental_type.fp_code + obj.code
            obj.code = code
        obj.save()


class FPLowerCat_Admin(admin.ModelAdmin):
    form = FPLowerCatForm
    list_display = (
        'id', 'name', 'code', 'fundamental_type', 'middle_category_type')
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

        (
            'Unique Code For This Finished Product Lower Category:', {
                'fields': ['code']}
        ),

    ]

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(FPLowerCat_Admin, self).get_form(request, obj, **kwargs)
    #     code = obj.code
    #     form.base_fields['code_edit'].initial = code
    #     return form

    def get_readonly_fields(self, request, obj=None):
        # This is the case when obj is already created i.e. it's an edit
        if obj:
            return ['code', 'fundamental_type', 'middle_category_type']
        else:
            return []

    def save_model(self, request, obj, form, change):

        if(not obj.id):
            code = obj.middle_category_type.code + obj.code
            obj.code = code
        obj.save()


class FPItem_Admin(admin.ModelAdmin):

    form = FPItemForm
    list_display = ('id', 'name', 'code', 'unit_price', 'fundamental_type',
                    'middle_category_type', 'lower_category_type')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = (
        'fundamental_type', 'middle_category_type', 'lower_category_type')
    fieldsets = [
        (
            'Name and Of The Production Item: ', {'fields': ['name', 'unit_price']}
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
            'Unique Code For This Finished Product Lower Category:', {
                'fields': ['code']}
        ),

        (
            'Check Box If This Finished Product Is A Compound Item:', {
                'fields': ['is_cp']}
        ),

    ]

    def get_readonly_fields(self, request, obj=None):
        # This is the case when obj is already created i.e. it's an edit
        if obj:
            return ['code', 'fundamental_type', 'middle_category_type', 'lower_category_type']
        else:
            return []

    def save_model(self, request, obj, form, change):

        if(not obj.id):
            if(obj.code):
                code = obj.lower_category_type.code + (obj.code).zfill(5)
                obj.code = code
            else:
                for i in range(1, 99999, 1):
                    temp = str(i).zfill(5)
                    temp_code = obj.lower_category_type.code + temp
                    if(FPItem.objects.filter(code=temp_code)):
                        continue
                    obj.code = temp_code
                    break

        obj.save()


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
