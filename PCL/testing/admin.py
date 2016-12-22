from django.contrib import admin

from testing.models import *


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('type', )

    class Media:
        js = ['/static/js/action_change.js']

admin.site.register(MyModel, MyModelAdmin)
