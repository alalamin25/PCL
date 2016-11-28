from django.contrib import admin
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.core.urlresolvers import reverse

from report.forms import FPReportForm
from report.models import FinishedProductReport
from report.util import FinishedProductReport_PDF


class FPReportForm_Admin(admin.ModelAdmin):
    # list_display = ('name',)
    form = FPReportForm


# admin.site.register(FinishedProductReport, FPReportForm_Admin)
# admin.site.register(FPReportForm)

class FinishedProductReport_Admin(admin.ModelAdmin):
    search_fields = ('name', )
    # list_filter = ( 'is_free', 'question_topic','subtopic1', )
    # list_display = ('id','question_set_text', 'uploader', 'is_free', 'question_topic','start_date', 'end_date',)
    # list_display_links = ('id', 'question_set_text',)

    filter_horizontal = ('fundamental_type', 'middle_category_type', 'lower_category_type')
    # raw_id_fields = ('question_topic', 'subtopic1', 'reading_topic', )
    # exclude = ('pub_date', 'edit_date')
    #
    def save_model(self, request, obj, form, change):
        print("\n\nGoing to download the PDF")
        response = FinishedProductReport_PDF(obj.name)
        print("\n Going to send the PDF\n\n")
        return HttpResponseRedirect("https://www.djangoproject.com")
        print("should have been redirected")

    def response_add(self, request, obj, post_url_continue="../%s/"):
        print("\n\n After add this method should be called")
        return HttpResponseRedirect('/report/fp_report')

    def response_change(self, request, obj):
        print("\n After change this method will be called\n")
        return HttpResponseRedirect('/report/fp_report')

    # return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))

admin.site.register(FinishedProductReport, FinishedProductReport_Admin)
