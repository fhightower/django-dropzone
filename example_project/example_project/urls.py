from django.conf import settings
from django.conf.urls import url, include
from django.views.static import serve

from. import views


urlpatterns = [
    url(r'^$', views.ExampleFormView.as_view()),
    url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:-1], serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^file_uploads/', include('file_uploads.urls')),
]
