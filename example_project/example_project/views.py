from django.views.generic import TemplateView


class ExampleView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(self, ExampleView).get_context_data(**kwargs)
        # context['form'] = form