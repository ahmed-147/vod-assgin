from django.urls import path, re_path
from .views import get_sites, FileUploadView


urlpatterns = [
    path('sites/', get_sites ),
    path('upload/sites/', FileUploadView.as_view() ),

    # re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
]
