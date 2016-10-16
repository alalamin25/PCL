from django.contrib import admin

from master_table.models import Suplier, FundamentalProductType, RawItem


class Suplier_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'edit_time')
    list_display_links = ('id', 'name',)
    list_filter = ('creation_time', 'edit_time',)
    search_fields = ('name',)
    fieldsets = [
        (
            'Name Of The Supplier: ', {'fields': ['name']}
        ),
        (
            'Address Of The Supplier: ', {'fields': ['address']}
        ),
        (
            'Phone Numbers:', {
                'fields': ['phone1', 'phone2', 'phone3', 'phone4', 'phone5']}
        ),
    ]


class FundamentalProductType_Admin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    fieldsets = [
        (
            'Name Of Fundamental Product: ', {'fields': ['name']}
        ),
    ]


class RawItem_Admin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('type',)
    fieldsets = [
        (
            'Name Of The Raw Material Item: ', {'fields': ['name']}
        ),
        (
            'Choose Fundamental Product Type For This Raw Item:', {
                'fields': ['type']}
        ),
        (
            'Write Comment: ', {'fields': ['comment']}
        ),

    ]

    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Suplier, Suplier_Admin)
admin.site.register(FundamentalProductType, FundamentalProductType_Admin)
admin.site.register(RawItem, RawItem_Admin)
