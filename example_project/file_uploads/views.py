import datetime
import json

from django.http import Http404, HttpResponse
from django.views.generic import View


class UploadView(View):
    def post(self, request):
        assert len(self.request.FILES) == 1

        from django.core.files.storage import default_storage

        field_name, tmp_file = self.request.FILES.items()[0]
        # TODO: Use "T" as date and time separator instead of space.
        with default_storage.open("user_uploads/" + str(datetime.datetime.now()) + "-" + tmp_file.name, "wb+") as f:
            for chunk in tmp_file.chunks():
                f.write(chunk)

            file_url = default_storage.url(f.name)

        return HttpResponse(json.dumps({"file_url": file_url}))
