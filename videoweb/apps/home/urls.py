from django.conf.urls.defaults import patterns, url

from django.conf import settings

urlpatterns = patterns('videoweb.apps.home.views',
                       url(r'^$', 'index_view', name='vista_principal'),
                       url(r'^about/', 'about_view', name='vista_about'),
                       url(r'^login/', 'login_view', name='vista_login'),
                       url(r'^logout/', 'logout_view', name='vista_logout'),
                       url(r'^upload/', 'uploadvideo_view', name='vista_uploadvideo'),
                       url(r'^myvideos/', 'myvideos_view', name='vista_myvideos'),
                       url(r'^newaccount/', 'newaccount_view', name='vista_newaccount'),
                       url(r'^register/', 'register_view'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )