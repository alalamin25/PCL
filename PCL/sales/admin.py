from django.contrib import admin

from sales.models import Credit, Sell, ExpenseDetail


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
        # (
        #     'Choose Middle Category Type For This Lower Category Finished Product: ', {
        #         'fields': ['middle_category_type']}
        # ),
        # (
        #     'Write Comment: ', {'fields': ['comment']}
        # ),

    ]


class Sell_Admin(admin.ModelAdmin):

    # change_form_template = 'commo/change_form.html'
    def get_form(self, request, obj=None, **kwargs):
        form = super(Sell_Admin, self).get_form(request, obj, **kwargs)
        form.base_fields['transection_no'].initial = 'abcd'
        return form


admin.site.register(Credit, Credit_Admin)
admin.site.register(Sell, Sell_Admin)
admin.site.register(ExpenseDetail, ExpenseDetail_Admin)
