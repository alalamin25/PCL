from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from homepage import views as homepage_views

admin.site.site_header = 'PCL ADMINISTRATION'
admin.site.site_title = "PCL Admin"


from testing.views import action_choices

urlpatterns = [

    # url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(
        template_name="homepage/index_page.html"), name='index'),
    url(r'^admin_home/$', login_required(TemplateView.as_view(template_name="homepage/admin_home_page.html"),
                                         login_url='/admin/login/'), name='admin_home'),

    url(r'^chaining/', include('smart_selects.urls')),
    # url(r'^report_builder/', include('report_builder.urls')),
    url(r'^report/', include('report.urls')),
    url(r'^ajax_request/', include('ajax_request.urls')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    # url(r'^select2/', include('django_select2.urls')),
    url(r'^action_choices/', action_choices),
]
