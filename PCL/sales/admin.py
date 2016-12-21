from django.contrib import admin

from sales.models import Credit, Sell


class Credit_Admin(admin.ModelAdmin):
    pass


class Sell_Admin(admin.ModelAdmin):

    # change_form_template = 'commo/change_form.html'
    def get_form(self, request, obj=None, **kwargs):
        form = super(Sell_Admin, self).get_form(request, obj, **kwargs)
        form.base_fields['transection_no'].initial = 'abcd'
        return form


admin.site.register(Credit, Credit_Admin)
admin.site.register(Sell, Sell_Admin)
