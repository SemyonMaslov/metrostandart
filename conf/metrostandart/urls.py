from django.urls import path
from metrostandart.views import (RenderHomeView, DocumentView, RenderLoginView,
                                 RenderRegisterView, logout_user)

urlpatterns = [
    path('', RenderHomeView.as_view(), name='home'),
    path('login/', RenderLoginView.as_view(), name='login'),
    path('register/', RenderRegisterView.as_view(), name='register'),
    path('document/', DocumentView.as_view(), name='document'),

    path('logout/', logout_user, name='logout'),
]
