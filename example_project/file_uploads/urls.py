from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(
        '^upload/$',
        views.UploadView.as_view(),
        name='upload',
    ),
)
