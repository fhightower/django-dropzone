*Please note, this is messy and unfinished, but the it works at least in the `example_project` setup.*

django-dropzone
=========================================

A simple Django widget for [Dropzonejs](http://www.dropzonejs.com/) ([http://www.dropzonejs.com/](http://www.dropzonejs.com/)).

Not yet pip installable.

Depends on Bootstrapm, jQuery and jquery.cookie.


Usage
=====


For usage, see the `example_project` Django project.

The beef is the `DropzoneInput`, which can be used as a form field. Example:
::

    from django.forms import Form
    from dropzone.forms import DropzoneInput
    
    
    class ExampleForm(Form):
        images = forms.FileField(
            widget=DropzoneInput(dropzone_config={
                "maxFilesize": 10,
                "acceptedFiles": "image/*",
                "url": '/file_uploads/upload/',
                "addRemoveLinks": True
            })
        )

You can pass configuration to Dropzonejs through the `dropzone_configuration` attribute. Refer to [http://www.dropzonejs.com/#configuration](http://www.dropzonejs.com/#configuration) available configuration.

You'll also need to add a bunch of static files somewhere in your html. Utilize `form.media` to include the main css and js. Bootstrap and jQuery dependencies are not included though. See example.html for an example.

The hardest part in using this, is that you'll need to implement an endpoint that can receive one file in an HTTP POST request and respond with json like `{"file_url": file_url}` where `file_url` is a the URL pointing to where the file can retrieved from.
Example: Create a Django view, handling that reads the file from `request.FILES` and uploads it to Amazon S3, grab the URL to the file from the S3 uploader and return `HttpResponse({"file_url": file_url})`.
