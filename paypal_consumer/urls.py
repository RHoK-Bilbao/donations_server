from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^setcheckout/$', 'paypal.views.setcheckout',
        {'return_url': 'http://tagmin.eu' + "/base/docheckout/",
         'cancel_url': 'http://tagmin.eu' + '/base/cancel/',
         'error_url': 'http://tagmin.eu' + '/base/error/',
         }, name = "paypal-setcheckout"),
                       
    url(r'^docheckout/$', 'paypal.views.docheckout',
        {'success_url': 'http://tagmin.eu' + "/base/success/",
         'error_url': 'http://tagmin.eu' + '/base/error/',
         }, name = "paypal-docheckout"),                       

    url(r'^dorefund/$', 'paypal.views.dorefund',
        {'success_url': 'http://tagmin.eu' + "/base/success/",
         'error_url': 'http://tagmin.eu' + '/base/error/',
         }, name = "paypal-dorefund"),
                       
    url(r'^cancel/$', 'paypal_consumer.views.cancel_page', name = "base-cancel"),
    url(r'^success/$', 'paypal_consumer.views.success_page', name = "base-success"),                       
    url(r'^error/$', 'paypal_consumer.views.error_page', name = "base-error"),
                       
)
