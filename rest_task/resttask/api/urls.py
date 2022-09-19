from django.urls import path
from .views import FileImportExportView, SiteList, api_overview,RequestList, RequestDetail

urlpatterns = [
    # path('sites/', get_sites),
    path('', api_overview),
    path('sites/', SiteList.as_view() ),
    path('sites/import/', FileImportExportView.as_view() ),
    path('sites/export/', FileImportExportView.as_view() ),
    path('requests/', RequestList.as_view()),
    path('requests/<int:pk>/', RequestDetail.as_view()),
]
