from django.contrib import admin

from master_table.models import Suplier


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

    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Suplier, Suplier_Admin)
# admin.site.register(Suplier)
