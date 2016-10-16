from django.contrib import admin
from entry_table.models import Purchase, Issue, Dispatch


class Purchase_Admin(admin.ModelAdmin):
    list_display = (
        'id', 'raw_item', 'suplier', 'unit_price', 'unit_amount', 'edit_time')
    list_display_links = ('id', )
    list_filter = ('creation_time', 'edit_time',)
    search_fields = ('raw_item', 'suplier')
    raw_id_fields = ('raw_item', 'suplier',)
    fieldsets = [
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


class Issue_Admin(admin.ModelAdmin):
    list_display = (
        'id', 'raw_item', 'unit_amount', 'edit_time')
    list_display_links = ('id', 'raw_item',)
    list_filter = ('creation_time', 'edit_time',)
    search_fields = ('raw_item',)
    raw_id_fields = ('raw_item',)
    fieldsets = [
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

class Dispatch_Admin(admin.ModelAdmin):
    list_display = (
        'id', 'raw_item', 'unit_amount', 'edit_time')
    list_display_links = ('id', 'raw_item',)
    list_filter = ('creation_time', 'edit_time',)
    search_fields = ('raw_item',)
    raw_id_fields = ('raw_item',)
    fieldsets = [
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


admin.site.register(Purchase, Purchase_Admin)
admin.site.register(Issue, Issue_Admin)
admin.site.register(Dispatch, Dispatch_Admin)
