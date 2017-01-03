from django.contrib import admin
from django import forms



from mother_godown.models import PurchaseEntry, IssueEntry
from django.core.exceptions import ValidationError


class PurchaseEntryForm(forms.ModelForm):

    class Meta:
        model = PurchaseEntry
        exclude = ()

    def clean(self):
        # Validation goes here :)
        supplier = self.cleaned_data.get('supplier')
        if(supplier and supplier.count() > 1):
            raise forms.ValidationError("You can select only one supplier")


class PurchaseEntry_Admin(admin.ModelAdmin):
    form = PurchaseEntryForm
    list_display = (
        'id', 'raw_item', 'fundamental_type', 'unit_price', 'unit_amount', 'date')
    list_display_links = ('id', 'raw_item')
    list_filter = ('fundamental_type', 'date', )
    search_fields = ('raw_item', 'supplier')
    filter_horizontal = ('supplier', )
    # raw_id_fields = ('supplier',)
    fieldsets = [
        (
            'Select Fundamental Product: ', {'fields': ['fundamental_type']}
        ),
        (
            'Name Of The Item: ', {'fields': ['raw_item']}
        ),
        (
            'Name Of The Supplier: ', {'fields': ['supplier']}
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

    # def save_model(self, request, obj, form, change):
    #     raise form.ValidationError("You can't assign more than 1 Supplier")

    # class Media:
    #     js = ('/static/js/limitchoice.js', )


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
