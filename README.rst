django-dropzone
=========================================

A simple django widget for dropzone.js

Allows you to use a dropzone.js uploader instead of the traditional HTML file upload widget.

Not yet pip installable.

Completely skinable.

*Please note, this is **messy and unfinished**. It might not even work properly right now. It you want to improve it, go ahead and submit a pull request.*


Usage
=====

An example form:
::

    class ExampleForm(forms.Form):
        image = forms.FileField(
                    widget=DropzoneInput(
                        maxFilesize=10,
                        acceptedFiles="image/*",
                        upload_path='/upload/file'
                    )
                )


Load in the following in your template:
::

  <link href="{% static "css/dropzone/dropzone.css" %}" type="text/css" rel="stylesheet" />

  <script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
  <script src="{% static "js/dropzone/dropzone.js" %}"></script>
  <script src="{% static "js/dropzone/dropzone.django.js" %}"></script>



**See the example project for more detail. I've not got around to writing this more thoroughly yet.**


Notes
=====
Currently only supports upload of one file at a time. Can be easily patched to support comma separated lists in the file_url input field.

Server must respond with a JSON dict on the file POST url. This dict should contain a "file_url" string which is the location of the file. i.e.
::

    class UploadFileView(View):
        def post(self, request, *args, **kwargs):
            posted_file = request.FILES.get('file')

            ...
            save file
            ...

            response = json.dumps({
                "file_url": path
            })

            return HttpResponse(response)