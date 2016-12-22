from django.contrib import admin

from sales.models import Credit, Sell, ExpenseDetail, SellDetailInfo


class ExpenseDetail_Admin(admin.ModelAdmin):

    list_display = (
        'date', 'deport_code', 'invoice_no', 'expense_criteria', 'amount', 'detail')
    search_fields = ('expense_criteria',)
    list_filter = ('date', 'expense_criteria', 'deport_code', )
    raw_id_fields = ('deport_code', )


class Credit_Admin(admin.ModelAdmin):
    list_display = (
        'date', 'serial_no', 'deport_code', 'customer_code', 'amount')
    search_fields = ('serial_no',)
    list_filter = ('date', 'deport_code', 'customer_code')
    raw_id_fields = ('deport_code', 'customer_code',)

    fieldsets = [
        (
            'Complete Basic Info: ', {'fields': ['serial_no', 'deport_code', 'customer_code',
                                                 'date', 'particular', 'payment_option']}
        ),
        (
            'If you have choosen payment option as Bank then fill these fields :', {
                'fields': ['bank', 'account_no']}
        ),
    ]


class SellDetailInfoInline(admin.TabularInline):
    # raw_id_fields = ('product_id', )
    model = SellDetailInfo
    extra = 0


class Sell_Admin(admin.ModelAdmin):
    list_display = (
        'date', 'transection_no', 'deport_code', 'customer_code', 'grand_total', 'total_commission', 'net_total')
    # search_fields = ('serial_no',)
    list_filter = ('date', 'deport_code')
    raw_id_fields = ('deport_code', 'customer_code')
    inlines = [SellDetailInfoInline]

    fieldsets = [
        (
            'Head Info: ', {'fields': ['transection_no', 'date', 'memo_no',
                                       'deport_code', 'customer_code',
                                       ]}
        ),
        # (
        #     'Detail Info :', {
        #         'fields': ['bank', 'account_no']}
        # ),
    ]
    # change_form_template = 'commo/change_form.html'

    def get_form(self, request, obj=None, **kwargs):
        form = super(Sell_Admin, self).get_form(request, obj, **kwargs)
        form.base_fields['transection_no'].initial = 'abcd'
        # self.initial['memo_no'] = self.transection_no
        return form


class SellDetailInfo_Admin(admin.ModelAdmin):
    list_display = (
        'rate', 'quantity', 'total')

    # raw_id_fields = ('product_id', )



admin.site.register(Credit, Credit_Admin)
admin.site.register(Sell, Sell_Admin)
admin.site.register(ExpenseDetail, ExpenseDetail_Admin)
admin.site.register(SellDetailInfo, SellDetailInfo_Admin)