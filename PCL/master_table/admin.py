from django.contrib import admin

from master_table.models import Suplier, FundamentalProductType,\
    RawItemMiddleCategory, RawItemLowerCategory, RawItem, Color,\
    FinishedProductItemMiddleCategory, FinishedProductItemLowerCategory,\
    FinishedProductItem, Shift, CompoundProductionItem,\
    CompoundProductionItemEntry


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


class Color_Admin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    fieldsets = [
        (
            'Name Of Color: ', {'fields': ['name']}
        ),
    ]


class RawItemMiddleCategory_Admin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('fundamental_type',)
    fieldsets = [
        (
            'Raw Material Middle Category Name: ', {'fields': ['name']}
        ),
        (
            'Choose Fundamental Product Type For This Raw Material Middle Category:', {
                'fields': ['fundamental_type']}
        ),
        (
            'Write Comment: ', {'fields': ['comment']}
        ),

    ]


class RawItemLowerCategory_Admin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('fundamental_type', 'middle_category_type',)
    fieldsets = [
        (
            'Raw Material Lower Category Name: ', {'fields': ['name']}
        ),
        (
            'Choose Fundamental Product Type For This Lower Category Raw Material :', {
                'fields': ['fundamental_type']}
        ),
        (
            'Choose Middle Category Type For This Lower Category Raw Material :', {
                'fields': ['middle_category_type']}
        ),
        (
            'Write Comment: ', {'fields': ['comment']}
        ),

    ]


class RawItem_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fundamental_type','middle_category_type', 'lower_category_type' )
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('fundamental_type',)
    fieldsets = [
        (
            'Name Of The Raw Material Item: ', {'fields': ['name']}
        ),
        (
            'Choose Fundamental Product Type For This Raw Item:', {
                'fields': ['fundamental_type']}
        ),
        (
            'Choose Fundamental Product Type For This Raw Item:', {
                'fields': ['fundamental_type']}
        ),
        (
            'Write Comment: ', {'fields': ['comment']}
        ),

    ]


class FinishedProductItemMiddleCategory_Admin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('fundamental_type',)
    fieldsets = [
        (
            'Finished Product Middle Category Name: ', {'fields': ['name']}
        ),
        (
            'Choose Fundamental Product Type For This Middle Category Finished Product:', {
                'fields': ['fundamental_type']}
        ),
        (
            'Write Comment: ', {'fields': ['comment']}
        ),

    ]


class FinishedProductItemLowerCategory_Admin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('fundamental_type', 'middle_category_type',)
    fieldsets = [
        (
            'Raw Material Lower Category Name: ', {'fields': ['name']}
        ),
        (
            'Choose Fundamental Product Type For This Lower Category Finished Product :', {
                'fields': ['fundamental_type']}
        ),
        (
            'Choose Middle Category Type For This Lower Category Finished Product: ', {
                'fields': ['middle_category_type']}
        ),
        (
            'Write Comment: ', {'fields': ['comment']}
        ),

    ]


class FinishedProductItem_Admin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('fundamental_type',)
    fieldsets = [
        (
            'Name Of The Production Item: ', {'fields': ['name']}
        ),
        (
            'Choose Fundamental Product Type For Production Item:', {
                'fields': ['fundamental_type']}
        ),
        (
            'Write Comment: ', {'fields': ['comment']}
        ),

    ]


class CompoundProductionItemEntryInline(admin.TabularInline):
    model = CompoundProductionItemEntry
    extra = 0


class CompoundProductionItem_Admin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('type',)
    inlines = [CompoundProductionItemEntryInline]
    fieldsets = [
        (
            'Name Of The Compound Production Item: ', {'fields': ['name']}
        ),
        (
            'Choose Fundamental Product Type For Production Item:', {
                'fields': ['type']}
        ),
        (
            'Write Comment: ', {'fields': ['comment']}
        ),

    ]


class Shift_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_time', 'end_time')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    fieldsets = [
        (
            'Name Of The Production Item: ', {'fields': ['name']}
        ),
        (
            'Select Start Time Of Shift(24 Hours format H:M:S): ', {
                'fields': ['start_time']}
        ),
        (
            'Select End Time Of Shift(24 Hours format H:M:S): ', {
                'fields': ['end_time']}
        ),
        (
            'Write Comment: ', {'fields': ['comment']}
        ),

    ]


admin.site.register(Suplier, Suplier_Admin)
admin.site.register(FundamentalProductType, FundamentalProductType_Admin)
admin.site.register(RawItemMiddleCategory, RawItemMiddleCategory_Admin)
admin.site.register(RawItemLowerCategory, RawItemLowerCategory_Admin)
admin.site.register(RawItem, RawItem_Admin)
admin.site.register(
    FinishedProductItemMiddleCategory, FinishedProductItemMiddleCategory_Admin)
admin.site.register(
    FinishedProductItemLowerCategory, FinishedProductItemLowerCategory_Admin)
admin.site.register(FinishedProductItem, FinishedProductItem_Admin)
admin.site.register(CompoundProductionItem, CompoundProductionItem_Admin)
admin.site.register(Color, Color_Admin)
admin.site.register(Shift, Shift_Admin)
