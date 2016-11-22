from django.conf.urls import include, url
from django.contrib import admin

from homepage.views import admin_home_page


urlpatterns = [
    # Examples:
    # url(r'^$', 'PCL.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', admin_home_page, name='admin_home_page'),
    url(r'^admin_home/$', admin_home_page, name='admin_home_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^report_builder/', include('report_builder.urls')),    
    url(r'^report/', include('report.urls')),

]
