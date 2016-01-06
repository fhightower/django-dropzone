import datetime
import json

from django.http import Http404, HttpResponse
from django.views.generic import View


class UploadView(View):
    def post(self, request):
        assert len(self.request.FILES) == 1

        from django.core.files.storage import default_storage

        field_name, tmp_file = self.request.FILES.items()[0]
        with default_storage.open("user_uploads/" + tmp_file.name + "-" + str(datetime.datetime.now()), "wb+") as f:
            for chunk in tmp_file.chunks():
                f.write(chunk)

            file_url = default_storage.url(f.name)

        return HttpResponse(json.dumps({"file_url": file_url}))
