from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bitcoin.views.home', name='home'),
    # url(r'^bitcoin/', include('bitcoin.foo.urls')),
    url(r'^test/$', views.test),
    url(r'^market/([A-Za-z\d]+)/$', views.market),    
    #url(r'^market/$', views.market),
    url(r'^bitcoin/$', views.bitcoin),
    url(r'^dropdown/$', views.dropdown),
    url(r'^update_alert/$', views.update_alert),
    url(r'^ohlc/$', views.ohlc),
    url(r'^index/$', views.index),
    url(r'^markets/$', views.markets),   
    url(r'^register/$', views.register), 
    url(r'^register_submit/$', views.register_submit), 
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
