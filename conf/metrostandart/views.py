import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from sendfile import sendfile

from metrostandart.models import User
from metrostandart.services.main import MainService


# Create your views here.

class RenderHomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'metrostandart/index.html')


class RenderLoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'metrostandart/login.html')

    def post(self, request, *args, **kwargs):
        user = authenticate(request, username=request.POST["login"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'metrostandart/login.html', context={
            'error': 'Не верный логин или пароль'
        })


class RenderRegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'metrostandart/register.html')

    def post(self, request, *args, **kwargs):
        User.objects.create_user(
            username=request.POST['login'],
            password=request.POST['password'],
            email=request.POST['email']
        )
        return redirect('login')


class DocumentView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/home/'

    def post(self, request):
        try:
            outcome = MainService.execute({}, {'file': request.FILES['file']})
            return sendfile(request, outcome, attachment=True,
                            attachment_filename=os.path.basename(outcome))
        except Exception as error:
            return render(request, 'metrostandart/index.html',
                          context={'error': str(error)})


def logout_user(request):
    logout(request)
    return redirect('home')
