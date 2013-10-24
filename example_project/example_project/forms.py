from django.forms import forms
from dropzone.forms import DropzoneInput

class ExampleForm(forms.Form):
    image = forms.FileField(widget=DropzoneInput(maxFilesize=10, acceptedFiles="image/*", upload_path='/upload/file', placeholder='Drop an image here!'))