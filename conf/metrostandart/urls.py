from django.urls import path
from metrostandart.views import RenderHomeView

urlpatterns = [
    path('', RenderHomeView.as_view()),
]
