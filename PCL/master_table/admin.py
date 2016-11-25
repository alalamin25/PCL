from django.contrib import admin

from master_table.models import Suplier, FundamentalProductType,\
    RawItem, FPMiddleCat, FPLowerCat,\
    FPItem, Shift, CPItem, CPItemEntry


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
    list_display = ('id', 'name', 'fundamental_type')
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
            'Write Comment: ', {'fields': ['comment']}
        ),

    ]


class FPMiddleCat_Admin(admin.ModelAdmin):
    list_display = ('id', 'name' , 'fundamental_type',)
    list_display_links = ('id', 'name')
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


class FPLowerCat_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fundamental_type', 'middle_category_type')
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


class FPItem_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fundamental_type', 'middle_category_type', 'lower_category_type')
    list_display_links = ('id', 'name')
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
            'Choose Middle Category For Production Item:', {
                'fields': ['middle_category_type']}
        ),
        (
            'Choose Lower Category For Production Item:', {
                'fields': ['lower_category_type']}
        ),
        (
            'Write Comment: ', {'fields': ['comment']}
        ),

    ]


class CPItemEntryInline(admin.TabularInline):
    model = CPItemEntry
    extra = 0


class CPItem_Admin(admin.ModelAdmin):
    list_display = ('id', 'fp_item',)
    list_display_links = ('id', 'fp_item',)
    search_fields = ('fp_item',)
    # list_filter = ('type',)
    inlines = [CPItemEntryInline]
    fieldsets = [
        (
            'Name Of The Compound Production Item: ', {'fields': ['fp_item']}
        ),

        (
            'Write Comment: ', {'fields': ['comment']}
        ),

    ]


class Shift_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fundamental_type', 'start_time', 'end_time')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('fundamental_type', )
    fieldsets = [
        (
            'Name Of The Production Item: ', {'fields': ['name']}
        ),
        (
            'Select Funtamental Product Type ', {
                'fields': ['fundamental_type']}
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
admin.site.register(RawItem, RawItem_Admin)
admin.site.register(FPMiddleCat, FPMiddleCat_Admin)
admin.site.register(FPLowerCat, FPLowerCat_Admin)
admin.site.register(FPItem, FPItem_Admin)
admin.site.register(CPItem, CPItem_Admin)
# admin.site.register(Color, Color_Admin)
admin.site.register(Shift, Shift_Admin)
admin.site.register(CPItemEntry)
