from django.contrib import admin
from mother_godown.models import PurchaseEntry, IssueEntry


class PurchaseEntry_Admin(admin.ModelAdmin):
    list_display = (
        'id', 'raw_item', 'fundamental_type', 'suplier', 'unit_price', 'unit_amount', 'edit_time')
    list_display_links = ('id', )
    list_filter = ('fundamental_type', 'creation_time', 'edit_time', )
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
                'fields': ['unit_price', 'unit_amount', 'invoice_no']}
        ),
        (
            'Write Comment:', {
                'fields': ['comment', ]}
        ),
    ]


class IssueEntry_Admin(admin.ModelAdmin):
    list_display = (
        'id', 'raw_item', 'fundamental_type', 'unit_amount', 'edit_time', 'creation_time',)
    list_display_links = ('id', 'raw_item',)
    list_filter = ('fundamental_type', 'creation_time', 'edit_time',)
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
            'Write Comment:', {
                'fields': ['comment', ]}
        ),
    ]



admin.site.register(PurchaseEntry, PurchaseEntry_Admin)
admin.site.register(IssueEntry, IssueEntry_Admin)

