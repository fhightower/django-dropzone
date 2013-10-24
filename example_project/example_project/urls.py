from django.conf.urls import patterns, url
from django.views.generic import TemplateView, FormView
from forms import ExampleForm

urlpatterns = patterns('',
    url(r'^$', FormView.as_view(template_name='example.html', form_class=ExampleForm))
)
