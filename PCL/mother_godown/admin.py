from django.contrib import admin
from mother_godown.models import PurchaseEntry, IssueEntry


class PurchaseEntry_Admin(admin.ModelAdmin):
    list_display = (
        'id', 'raw_item', 'fundamental_type', 'suplier', 'unit_price', 'unit_amount', 'date')
    list_display_links = ('id', 'raw_item')
    list_filter = ('fundamental_type', 'date', )
    search_fields = ('raw_item', 'suplier')
    raw_id_fields = ('suplier',)
    fieldsets = [
        (
            'Select Fundamental Product: ', {'fields': ['fundamental_type']}
        ),
        (
            'Name Of The Item: ', {'fields': ['raw_item']}
        ),
        (
            'Name Of The Supplier: ', {'fields': ['suplier']}
        ),
        (
            'Enter Details: ', {
                'fields': ['unit_price', 'unit_type', 'unit_amount', 'invoice_no']}
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


class IssueEntry_Admin(admin.ModelAdmin):
    list_display = (
        'id', 'raw_item', 'fundamental_type', 'unit_amount', 'date',)
    list_display_links = ('id', 'raw_item',)
    list_filter = ('fundamental_type', 'date',)
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


admin.site.register(PurchaseEntry, PurchaseEntry_Admin)
admin.site.register(IssueEntry, IssueEntry_Admin)
