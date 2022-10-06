from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.urls import path
from . import views

app_name = 'temperature'
urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    path('', views.ChartFormView.as_view(), name='chart_form_view'),
    path('list', views.TemperatureListView.as_view(), name='list_view'),
]
