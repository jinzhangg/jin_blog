from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jin_blog.views.home', name='home'),
    # url(r'^jin_blog/', include('jin_blog.foo.urls')),
    url(r"^$", "jin_blog.views.home", name="home"),

    url(r'^admin/', include(admin.site.urls)),
)
