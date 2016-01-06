from django.conf import settings
from django.conf.urls import patterns, url, include
from django.views.generic import FormView
from forms import ExampleForm


urlpatterns = patterns('',
    url(r'^$', FormView.as_view(template_name='example.html', form_class=ExampleForm)),
    url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:-1], 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^file_uploads/', include('file_uploads.urls')),
)
