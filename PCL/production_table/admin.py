from django.contrib import admin
from production_table.models import ProductionEntry, RawItemEntry,\
    RIIssueEntry, RIReturnEntry


class ProductionEntry_Admin(admin.ModelAdmin):

    list_display = (
        'id', 'finished_product_item', 'fundamental_type', 'shift',
        'unit_amount', 'date')
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
                'fields': ['unit_amount', 'invoice_no']}
        ),

        (
            'Select Date:', {
                'fields': ['date', ]}
        ),


        (
            'Write Comment:', {
                'fields': ['comment', ]}
        ),
    ]


class RawItemEntry_Admin(admin.ModelAdmin):
    list_display = (
        'id', 'raw_item', 'fundamental_type', 'unit_amount', 'date',)
    list_display_links = ('id', 'raw_item',)
    list_filter = ( 'fundamental_type', 'date',)
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
            'Enter Details: ', {
                'fields': ['unit_amount', 'invoice_no']}
        ),

        (
            'Select Date:', {
                'fields': ['date', ]}
        ),

        (
            'Write Comment:', {
                'fields': ['comment', ]}
        ),
    ]


class RIIssueEntry_Admin(admin.ModelAdmin):

    list_display = (
        'id', 'raw_item', 'fundamental_type', 'shift', 'unit_amount', 'date',)
    list_display_links = ('id', 'raw_item',)
    list_filter = ( 'fundamental_type', 'shift', 'date',)
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
                'fields': ['unit_amount']}
        ),

        (
            'Select Date:', {
                'fields': ['date', ]}
        ),

        (
            'Write Comment:', {
                'fields': ['comment', ]}
        ),
    ]


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
                'fields': ['unit_amount']}
        ),
        (
            'Select Date:', {
                'fields': ['date', ]}
        ),

        
        (
            'Write Comment:', {
                'fields': ['comment', ]}
        ),
    ]


admin.site.register(ProductionEntry, ProductionEntry_Admin)
admin.site.register(RawItemEntry, RawItemEntry_Admin)
admin.site.register(RIIssueEntry, RIIssueEntry_Admin)
admin.site.register(RIReturnEntry, RIReturnEntry_Admin)
