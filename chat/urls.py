from django.conf.urls import patterns, url


urlpatterns = patterns('chat.views',
    url(r'^$', 'echo'),
    url(r'^ws/$', 'echo_ws'),
)
