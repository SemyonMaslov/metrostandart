from django.urls import path
from metrostandart.views import RenderHomeView, DocumentView

urlpatterns = [
    path('', RenderHomeView.as_view()),
    path('document/', DocumentView.as_view(), name='document'),
]
