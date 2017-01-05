from django.contrib import admin
from production_table.models import ProductionEntry, RawItemEntry,\
    RIIssueEntry, RIReturnEntry

from production_table.forms import RIIssueEntryForm, RawItemEntryForm,\
    RIReturnEntryForm, ProductionEntryForm


class ProductionEntry_Admin(admin.ModelAdmin):

    form = ProductionEntryForm
    list_display = (
        'id', 'fp_item', 'fundamental_type', 'shift',
        'get_unit_amount', 'date')
    list_display_links = ('id', 'fp_item',)
    list_filter = ('fundamental_type', 'shift', 'date',)
    search_fields = ('fp_item__name', 'fp_item__code')
    filter_horizontal = ('fp_item_many',)
    fieldsets = [
        (
            'Select The Shift: ', {'fields': ['fundamental_type', 'shift']}
        ),

        (
            'Select Finished Item By Searching:', {
                'fields': ['fp_item_many', ]}
        ),

        (
            'Select Finished Item Info: ',
            {'fields': ['middle_category_type',
                        'lower_category_type', 'fp_item_chained']}
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
        fp_item_many = form.cleaned_data.get('fp_item_many')
        if(fp_item_many):
            obj.fp_item = fp_item_many[0]
        if(obj.fp_item_chained):
            obj.fp_item = obj.fp_item_chained
        obj.save()


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

    form = RIReturnEntryForm
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


admin.site.register(ProductionEntry, ProductionEntry_Admin)
admin.site.register(RawItemEntry, RawItemEntry_Admin)
admin.site.register(RIIssueEntry, RIIssueEntry_Admin)
admin.site.register(RIReturnEntry, RIReturnEntry_Admin)
