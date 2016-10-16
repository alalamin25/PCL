from django.contrib import admin
from production_table.models import ProductionEntry


class ProductionEntry_Admin(admin.ModelAdmin):

    list_display = (
        'id', 'production_item', 'compound_production_item', 'shift',
        'unit_amount', 'edit_time')
    list_display_links = ('id', 'production_item',)
    list_filter = ('shift', 'creation_time', 'edit_time',)
    search_fields = ('production_item',)
    raw_id_fields = ('production_item', 'compound_production_item',)
    fieldsets = [
        (
            'Select Name Of The Production Item: ', {
                'fields': ['production_item']}
        ),
        (
            'Select Name Of The Complex Production Item(If you have selected \
            Production Item then you dont need to select this): ', {
                'fields': ['compound_production_item']}
        ),
        (
            'Select Shift: ', {'fields': ['shift']}
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


admin.site.register(ProductionEntry, ProductionEntry_Admin)
