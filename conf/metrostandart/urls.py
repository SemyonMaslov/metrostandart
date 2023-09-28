from django.urls import path
from metrostandart.views import (RenderHomeView, DocumentView, RenderLoginView,
                                 RenderRegisterView)

urlpatterns = [
    path('', RenderHomeView.as_view(), name='home'),
    path('auth/login/', RenderLoginView.as_view(), name='login'),
    path('auth/register/', RenderRegisterView.as_view(), name='register'),
    path('document/', DocumentView.as_view(), name='document'),
]
