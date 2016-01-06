import datetime

from django.http import Http404, HttpResponse
from django.views.generic import View


class UploadView(View):
    def post(self, request):
        from django.core.files.storage import default_storage

        file_urls = []

        for field_name, tmp_file in self.request.FILES.items():
            with default_storage.open("user_uploads/" + tmp_file.name + "-" + str(datetime.datetime.now()), "wb+") as f:
                for chunk in tmp_file.chunks():
                    f.write(chunk)

                file_urls.append(default_storage.url(f.name))

        return HttpResponse("")
