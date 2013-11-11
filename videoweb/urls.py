from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('videoweb.apps.home.views',
                       url(r'^$', 'index_view', name='vista_principal'),
                       url(r'^about/', 'about_view', name='vista_about'),
                       url(r'^login/', 'login_view', name='vista_login'),
                       url(r'^logout/', 'logout_view', name='vista_logout'),
                       url(r'^upload/', 'uploadvideo_view', name='vista_uploadvideo'),
                       url(r'^myvideos/', 'myvideos_view', name='vista_myvideos'),
                       url(r'^newaccount/', 'newaccount_view', name='vista_newaccount'),
                       url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns = patterns('',
    # Examples:
    #url(r'^$', include('videoweb.apps.home.urls')),
    #url(r'^', include('videoweb.apps.home.urls')),
    #url(r'^', include('videoweb.apps.conversion.urls')),
    #url(r'^$', 'videoweb.views.home', name='home'),
    #url(r'^videoweb/', include('videoweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
#)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )