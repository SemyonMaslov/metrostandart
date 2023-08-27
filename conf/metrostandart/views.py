import os

from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.views import View
from sendfile import sendfile

from metrostandart.services.main import MainService


# Create your views here.

class RenderHomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'metrostandart/index.html')


class DocumentView(View):

    def post(self, request):
        try:
            outcome = MainService.execute({}, {'file': request.FILES['file']})
            return sendfile(request, outcome, attachment=True, attachment_filename=os.path.basename(outcome))
        except Exception as error:
            return render(request, 'metrostandart/index.html', context={'error': str(error)})
