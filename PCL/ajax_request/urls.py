from django.conf.urls import url



from ajax_request import views
# from django.views.generic import TemplateView


urlpatterns = [

    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^deport/$', views.DeportView.as_view(), name='deport'),
    # url(r'^fp_report/middle_cat$',
    #     views.FpMiddleCatView.as_view(), name='fp_middle_cat'),
    # url(r'^fp_report/lower_cat$', views.FpLowerCatView.as_view(),
    #     name='fp_lower_cat'),
    # url(r'^fp_report/fpitem$', views.FpItemView.as_view(),
    #     name='fp_item'),
    # url(r'^fp_report/report$', views.FpItemReportView.as_view(),
    #     name='fp_item_report'),

    # url(r'^shiftwise/$', views.ShiftWiseView.as_view(), name='shiftwise'),
    # url(r'^shiftwise/select$', views.ShiftSelectView.as_view(), name='shiftselect'),
    # url(r'^shiftwise/report$', views.ShiftWiseReportView.as_view(),
    #     name='shfitwise_report'),

    # url(r'^rawitem/$', views.RawItemView.as_view(), name='rawitem'),
    # url(r'^rawitem/select$', views.RawItemSelectView.as_view(), name='rawitem_select'),
    # url(r'^rawitem/report$', views.RawItemReportView.as_view(),
    #     name='rawitem_report'),


    # url(r'^fp_report/report$', views.HelloPDFView.as_view(),
    #     name='fp_item_report'),
]
