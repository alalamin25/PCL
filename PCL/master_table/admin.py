from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from master_table.models import Suplier, FundamentalProductType,\
    RawItem, FPMiddleCat, FPLowerCat, ExpenseCriteria,\
    FPItem, Shift, CPItem, CPItemEntry, Deport, Customer, Deport,\
    BankAccount, Bank


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
    ]


class Suplier_Admin(admin.ModelAdmin):
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
            'Name Of The Supplier: ', {'fields': ['name']}
        ),
        (
            'Select What Type Of Raw Material This Supplier Provides: ', {'fields': ['fundamental_type']}
        ),
        (
            'Address Of The Supplier: ', {'fields': ['address']}
        ),
        (
            'Phone Numbers:', {
                'fields': ['phone1', 'phone2', 'phone3', 'phone4', 'phone5']}
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
        # (
        #     'Write Comment: ', {'fields': ['comment']}
        # ),

    ]


class FPMiddleCat_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fundamental_type',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('fundamental_type',)
    fieldsets = [
        (
            'Finished Product Middle Category Name: ', {'fields': ['name']}
        ),
        (
            'Choose Fundamental Product Type For This Middle Category Finished Product:', {
                'fields': ['fundamental_type']}
        ),
        # (
        #     'Write Comment: ', {'fields': ['comment']}
        # ),

    ]


class FPLowerCat_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fundamental_type', 'middle_category_type')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('fundamental_type', 'middle_category_type',)
    fieldsets = [
        (
            'Raw Material Lower Category Name: ', {'fields': ['name']}
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
    list_filter = ('fundamental_type', 'middle_category_type', 'lower_category_type')
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


admin.site.register(Suplier, Suplier_Admin)
admin.site.register(FundamentalProductType, FundamentalProductType_Admin)
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
