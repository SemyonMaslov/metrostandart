from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View


# Create your views here.

class RenderHomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'metrostandart/index.html')

