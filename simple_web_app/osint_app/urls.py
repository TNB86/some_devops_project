from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_collect, name='collect_data'),
    path('waiting/', views.waiting, name='waiting'),
    path('report/', views.report, name='report'),
    path('report/download/<str:filename>', views.download_file, name='download_file'),
]