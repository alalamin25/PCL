from django.contrib import admin

from sales.models import Payment, Sell, ExpenseDetail, SellDetailInfo, DeportOperation
from django.forms import TextInput, Textarea
from django.db import models
from sales.forms import ExpenseDetailForm, PaymentForm, DeportOperationForm, SellForm, SellDetailInfoForm


class ExpenseDetail_Admin(admin.ModelAdmin):

    form = ExpenseDetailForm
    list_display = (
        'id', 'date', 'get_deport', 'invoice_no', 'get_expense_criteria', 'amount', 'detail')
    list_display_links = list_display
    search_fields = ('expense_criteria',)
    list_filter = ('date', 'expense_criteria', 'deport', )
    filter_horizontal = ('deport', 'expense_criteria')


class Payment_Admin(admin.ModelAdmin):

    form = PaymentForm
    list_display = (
        'id', 'date', 'serial_no', 'deport', 'get_customer', 'amount')
    list_display_links = list_display
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

# class SellDetailInfoInline(admin.StackedInline):


class SellDetailInfoInline(admin.TabularInline):
    raw_id_fields = ('product_code', )
    # readonly_fields = ('product_code_text',)
    fields = ('id', 'product_code', 'product_code_text', 'fundamental_type',
              'middle_category_type', 'lower_category_type', 'finished_product_item', 'rate', 'quantity',
              'total', 'commission', 'net_total', )

    model = SellDetailInfo
    extra = 0


class Sell_Admin(admin.ModelAdmin):

    form = SellForm
    filter_horizontal = ('customer',)
    list_display = (
        'id', 'date', 'transection_no', 'memo_no', 'deport', 'get_customer_name', 'grand_total',
        'total_commission', 'net_total')
    list_display_links = list_display
    list_display_links = list_display
    search_fields = ('memo_no', 'deport__name', 'customer__name')
    list_filter = ('date', 'deport')
    # raw_id_fields = ( 'customer_code')
    inlines = [SellDetailInfoInline]
    # StackedInline = [SellDetailInfoInline]
    # filter_horizontal = ('deport',)

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
        latest_sell = Sell.objects.all().order_by('-id').first()
        if(latest_sell):
            latest_sell = latest_sell.id + 1
        else:
            latest_sell = 1
        form.base_fields['transection_no'].initial = str(latest_sell)
        form.base_fields['memo_no'].initial = str(latest_sell)
        return form

    class Media:
        js = ['/static/sales/js/sales.js']


class SellDetailInfo_Admin(admin.ModelAdmin):

    form = SellDetailInfoForm

    list_display = (
        'id', 'product_code', 'get_memo_no', 'rate', 'quantity', 'total')
    # list_display_links = list_display
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '5'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }
    # raw_id_fields = ('product_id', )


class DeportOperation_Admin(admin.ModelAdmin):

    form = DeportOperationForm
    list_display = (
        'id', 'date', 'deport_operation', 'deport_code', 'fp_item', 'quantity')
    # search_fields = ('serial_no',)
    list_display_links = list_display
    list_filter = ('date', 'deport_code')
    raw_id_fields = ('memo_no',)
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
                'fields': ['customer', 'return_rate', 'memo_no']}
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

    class Media:
        js = ['/static/sales/js/deport_operation.js']


admin.site.register(Payment, Payment_Admin)
admin.site.register(Sell, Sell_Admin)
admin.site.register(ExpenseDetail, ExpenseDetail_Admin)
admin.site.register(SellDetailInfo, SellDetailInfo_Admin)
admin.site.register(DeportOperation, DeportOperation_Admin)
