from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('userena.urls')),
    (r'^rosetta/', include('rosetta.urls')),
    (r'^markitup/', include('markitup.urls')),

    (r'^$', TemplateView.as_view(template_name="hello.html"))
)
