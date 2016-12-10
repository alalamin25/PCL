from report import views

from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(
        template_name="report/index.html"), name='index'),
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^fp_report/$', views.FpReportView.as_view(), name='fp_report'),
    url(r'^fp_report/middle_cat$',
        views.FpMiddleCatView.as_view(), name='fp_middle_cat'),
    url(r'^fp_report/lower_cat$', views.FpLowerCatView.as_view(),
        name='fp_lower_cat'),
    url(r'^fp_report/fpitem$', views.FpItemView.as_view(),
        name='fp_item'),
    url(r'^fp_report/report$', views.FpItemReportView.as_view(),
        name='fp_item_report'),

    url(r'^shiftwise/$', views.ShiftWiseView.as_view(), name='shiftwise'),
    url(r'^shiftselect/$', views.ShiftSelectView.as_view(), name='shiftselect'),
    url(r'^shiftwise/report$', views.ShiftWiseReportView.as_view(),
        name='shfitwise_report'),


    # url(r'^fp_report/report$', views.HelloPDFView.as_view(),
    #     name='fp_item_report'),
]
