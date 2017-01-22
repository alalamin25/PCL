from django.contrib import admin

from sales.models import Payment, Sell, ExpenseDetail, SellDetailInfo, DeportOperation
from django.forms import TextInput, Textarea
from django.db import models
from sales.forms import ExpenseDetailForm, PaymentForm, DeportOperationForm, SellForm, SellDetailInfoForm


class ExpenseDetail_Admin(admin.ModelAdmin):

    form = ExpenseDetailForm
    list_display = (
        'date', 'get_deport','invoice_no', 'get_expense_criteria', 'amount', 'detail')
    search_fields = ('expense_criteria',)
    list_filter = ('date', 'expense_criteria', 'deport', )
    filter_horizontal = ('deport', 'expense_criteria')


class Payment_Admin(admin.ModelAdmin):

    form = PaymentForm
    list_display = (
        'date', 'serial_no', 'deport', 'get_customer', 'amount')
    search_fields = ('serial_no',)
    list_filter = ('date', 'deport')
    # raw_id_fields = ( 'customer_code',)
    # readonly_fields = ('deport_code_text',)
    filter_horizontal = ('customer',)
    fieldsets = [
        (
            'Complete Basic Info: ',
            {'fields': ['serial_no',
                        'transection_no',
                        ('deport'),
                        'customer',
                        'date', 'particular',
                        'amount',
                        'payment_option']}
        ),
        (
            'If you have choosen payment option as Bank then fill these fields :', {
                'fields': ['bank', 'account_no']}
        ),
    ]

    class Media:
        js = ['/static/js/custom.js']


class SellDetailInfoInline(admin.TabularInline):
    raw_id_fields = ('product_code', )
    model = SellDetailInfo
    extra = 0


class Sell_Admin(admin.ModelAdmin):

    form = SellForm
    filter_horizontal = ('customer',)
    list_display = (
        'date', 'transection_no', 'deport', 'get_customer', 'grand_total', 'total_commission', 'net_total')
    search_fields = ('transection_no', 'memo_no')
    list_filter = ('date', 'deport')
    # raw_id_fields = ( 'customer_code')
    inlines = [SellDetailInfoInline]

    fieldsets = [
        (
            'Head Info: ', {'fields': ['transection_no', 'date', 'memo_no',
                                       'deport', 'customer',
                                       ]}
        ),
        (
            'Calculation :', {
                'fields': ['grand_total', 'total_commission', 'net_total']}
        ),
    ]
    # change_form_template = 'commo/change_form.html'


    def get_form(self, request, obj=None, **kwargs):
        form = super(Sell_Admin, self).get_form(request, obj, **kwargs)
        form.base_fields['transection_no'].initial = 'abcd'
        # self.initial['memo_no'] = self.transection_no
        return form

    class Media:
        js = ['/static/sales/js/sales.js']


class SellDetailInfo_Admin(admin.ModelAdmin):

    form = SellDetailInfoForm


    list_display = (
         'product_code', 'rate', 'quantity', 'total')

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '5'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }
    # raw_id_fields = ('product_id', )


class DeportOperation_Admin(admin.ModelAdmin):

    form = DeportOperationForm
    list_display = (
        'date', 'deport_operation', 'deport_code', 'fp_item', 'quantity')
    # search_fields = ('serial_no',)
    list_filter = ('date', 'deport_code')
    raw_id_fields = ('transection_no',)
    filter_horizontal = ('fp_item_many', 'customer')
    fieldsets = [
        (
            'Basic Info: ', {
                'fields': ['deport_operation', 'deport_code',  'date', 'quantity']}
        ),

        (
            'Select Finished Item By Searching:', {
                'fields': ['fp_item_many', ]}
        ),
        (
            'Select Product by Chaining', {'fields': [
                'fundamental_type', 'middle_category_type',  'lower_category_type',
                'fp_item_chained', ]}
        ),

        # (
        #     'Select Product by Product Code: ', {'fields': ['fp_item', ]}
        # ),

        (
            'If Deport Operation is From Other Deport Then Fill this up :', {
                'fields': ['deport_from_code', ]}
        ),

        (
            'If Deport Operation is Sales Return Then Fill this up :', {
                'fields': ['customer', 'return_rate', 'transection_no']}
        ),
    ]

    def save_model(self, request, obj, form, change):

        obj.save()
        fp_item_many = form.cleaned_data.get('fp_item_many')
        if(fp_item_many):
            obj.fp_item = fp_item_many[0]
        if(obj.fp_item_chained):
            obj.fp_item = obj.fp_item_chained
        obj.save()



admin.site.register(Payment, Payment_Admin)
admin.site.register(Sell, Sell_Admin)
admin.site.register(ExpenseDetail, ExpenseDetail_Admin)
# admin.site.register(SellDetailInfo, SellDetailInfo_Admin)
admin.site.register(DeportOperation, DeportOperation_Admin)
