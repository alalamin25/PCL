from django.contrib import admin
from production_table.models import ProductionEntry, RawItemEntry,\
    RIIssueEntry, RIReturnEntry

from production_table.forms import RIIssueEntryForm, RawItemEntryForm


class ProductionEntry_Admin(admin.ModelAdmin):

    list_display = (
        'id', 'finished_product_item', 'fundamental_type', 'shift',
        'get_unit_amount', 'date')
    list_display_links = ('id', 'finished_product_item',)
    list_filter = ('fundamental_type', 'shift', 'date',)
    search_fields = ('finished_product_item',)
    fieldsets = [
        (
            'Select Fundamental Product: ', {'fields': ['fundamental_type']}
        ),
        (
            'Select Name Of The Production Item: ', {
                'fields': ['finished_product_item']}
        ),

        (
            'Select Shift: ', {'fields': ['shift']}
        ),

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


class RawItemEntry_Admin(admin.ModelAdmin):
    form = RawItemEntryForm
    list_display = (
        'id', 'raw_item', 'unit_amount', 'date',)
    list_display_links = ('id', 'raw_item',)
    list_filter = ('fundamental_type', 'date',)
    search_fields = ('raw_item__name', 'raw_item__code')
    filter_horizontal = ('raw_item_many',)
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


class RIIssueEntry_Admin(admin.ModelAdmin):

    form = RIIssueEntryForm
    list_display = (
        'id', 'raw_item', 'fundamental_type', 'shift', 'unit_amount', 'date',)
    list_display_links = ('id', 'raw_item',)
    list_filter = ('fundamental_type', 'shift', 'date',)
    search_fields = ('raw_item__name', 'raw_item__code')
    # raw_id_fields = ('raw_item',)
    filter_horizontal = ('raw_item_many',)
    fieldsets = [
        (
            'Select The Shift: ', {'fields': ['fundamental_type', 'shift']}
        ),

        (
            'Select Raw Item By Searching:', {
                'fields': ['raw_item_many', ]}
        ),

        (
            'Select Raw Item Info: ',
            {'fields': ['middle_category_type',
                        'lower_category_type', 'raw_item_chained']}
        ),

        (
            'Enter Details: ', {
                'fields': ['unit_type', 'unit_amount']}
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


class RIReturnEntry_Admin(admin.ModelAdmin):

    list_display = (
        'id', 'raw_item', 'fundamental_type', 'shift', 'unit_amount', 'date',)
    list_display_links = ('id', 'raw_item',)
    list_filter = ('fundamental_type', 'shift', 'date',)
    search_fields = ('raw_item',)
    # raw_id_fields = ('raw_item',)
    fieldsets = [
        (
            'Select Fundamental Product: ', {'fields': ['fundamental_type']}
        ),
        (
            'Name Of The Item: ', {'fields': ['raw_item']}
        ),
        (
            'Select The Shift: ', {'fields': ['shift']}
        ),
        (
            'Enter Details: ', {
                'fields': ['unit_type', 'unit_amount']}
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


admin.site.register(ProductionEntry, ProductionEntry_Admin)
admin.site.register(RawItemEntry, RawItemEntry_Admin)
admin.site.register(RIIssueEntry, RIIssueEntry_Admin)
admin.site.register(RIReturnEntry, RIReturnEntry_Admin)
