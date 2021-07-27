from django.urls import path
from .views import link_shorter, redirector
urlpatterns = [
    path('', link_shorter),
    path('s/<args>', redirector),
]