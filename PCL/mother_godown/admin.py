from django.contrib import admin

from mother_godown.models import PurchaseEntry, IssueEntry
from django.core.exceptions import ValidationError

from mother_godown.forms import PurchaseEntryForm, IssueEntryForm


class PurchaseEntry_Admin(admin.ModelAdmin):
    form = PurchaseEntryForm
    list_display = (
        'id', 'raw_item', 'unit_price', 'unit_amount', 'total_price', 'date')
    list_display_links = ('id', 'raw_item')
    list_filter = ('fundamental_type', 'date', )
    search_fields = ('raw_item__name', 'raw_item__code')
    filter_horizontal = ('supplier', 'raw_item_many')
    # raw_id_fields = ('supplier',)
    fieldsets = [

        (
            'Select Raw Item By Searching:', {
                'fields': ['raw_item_many', ]}
        ),

        (
            'Select Raw Item Info: ',
            {'fields': ['fundamental_type', 'middle_category_type',
                        'lower_category_type', 'raw_item_chained']}
        ),
        (
            'Name Of The Supplier: ', {'fields': ['supplier']}
        ),
        (
            'Enter Details: ', {
                'fields': ['unit_price', 'unit_type', 'unit_amount', 'total_price', 'invoice_no']}
        ),

        (
            'Select Date:', {
                'fields': ['date', ]}
        ),


        (
            'Write Comment:', {
                'fields': ['enroll_comment_in_report', 'comment', ]}
        ),
    ]

    def save_model(self, request, obj, form, change):

        obj.save()
        raw_item_many = form.cleaned_data.get('raw_item_many')
        if(raw_item_many):
            obj.raw_item = raw_item_many[0]
        if(obj.raw_item_chained):
            obj.raw_item = obj.raw_item_chained
        obj.save()

    class Media:
        js = ('/static/mother_godown/js/calculate_total.js', )


class IssueEntry_Admin(admin.ModelAdmin):
    form = IssueEntryForm
    list_display = (
        'id', 'raw_item', 'unit_amount', 'date',)
    # list_display_links = ('id', 'raw_item__name',)
    list_filter = ('fundamental_type', 'date',)
    search_fields = ('raw_item__name', 'raw_item__code')
    filter_horizontal = ('raw_item_many', )
    # raw_id_fields = ('raw_item',)
    fieldsets = [

        (
            'Select Raw Item By Searching:', {
                'fields': ['raw_item_many', ]}
        ),

        (
            'Select Raw Item Info: ',
            {'fields': ['fundamental_type', 'middle_category_type',
                        'lower_category_type', 'raw_item_chained']}
        ),
        # (
        #     'Name Of The Item: ', {'fields': ['raw_item']}
        # ),
        (
            'Enter Details: ', {
                'fields': ['unit_type', 'unit_amount', 'invoice_no']}
        ),
        (
            'Select Date:', {
                'fields': ['date', ]}
        ),
        (
            'Write Comment:', {
                'fields': ['enroll_comment_in_report', 'comment', ]}
        ),
    ]

    def save_model(self, request, obj, form, change):

        obj.save()
        raw_item_many = form.cleaned_data.get('raw_item_many')
        if(raw_item_many):
            obj.raw_item = raw_item_many[0]
        if(obj.raw_item_chained):
            obj.raw_item = obj.raw_item_chained
        obj.save()

admin.site.register(PurchaseEntry, PurchaseEntry_Admin)
admin.site.register(IssueEntry, IssueEntry_Admin)
