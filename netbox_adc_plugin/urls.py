from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("adcs/", views.ADCListView.as_view(), name="adc_list"),
    path("adcs/add/", views.ADCEditView.as_view(), name="adc_add"),
    path("adcs/<int:pk>/", views.ADCView.as_view(), name="adc"),
    path("adcs/<int:pk>/edit/", views.ADCEditView.as_view(), name="adc_edit"),
    path("adcs/<int:pk>/delete/", views.ADCDeleteView.as_view(), name="adc_delete"),
    path(
        "adcs/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="adc_changelog",
        kwargs={"model": models.ADC},
    ),
)
