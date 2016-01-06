from django.conf import settings
from django.conf.urls import patterns, url, include
import views


urlpatterns = patterns('',
    url(r'^$', views.ExampleFormView.as_view()),
    url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:-1], 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^file_uploads/', include('file_uploads.urls')),
)
