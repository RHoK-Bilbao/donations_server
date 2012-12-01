from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
    url(r'^base/', include("paypal_consumer.urls")),
    url(r'^$', "django.views.generic.simple.redirect_to", {"url": "/base/setcheckout/"})  
)
