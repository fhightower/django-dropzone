from django.views.generic import FormView

from forms import ExampleForm


class ExampleFormView(FormView):
    template_name = 'example.html'
    form_class = ExampleForm

    def get_initial(self):
        return {
            "images": "http://localhost:8001/media/user_uploads/2016-01-06 13:30:12.432073-"
                      "Dressage-Mastery-Academy-Dressage-Explained-Part-2-Losgelassenheit-Mindset.pdf,"
                      "http://localhost:8001/media/user_uploads/2016-01-06 08:02:00.185925-IMG_20160104_215821.jpg"
        }

    def get(self, *args, **kwargs):
        return super(ExampleFormView, self).get(*args, **kwargs)
