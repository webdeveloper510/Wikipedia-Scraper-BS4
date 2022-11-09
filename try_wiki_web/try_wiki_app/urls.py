from django.urls import path
from . import views
urlpatterns = [
    path('' , views.scrape_results_type),
]
