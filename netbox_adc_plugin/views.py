from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class ADCView(generic.ObjectView):
    queryset = models.ADC.objects.all()


class ADCListView(generic.ObjectListView):
    queryset = models.ADC.objects.all()
    table = tables.ADCTable


class ADCEditView(generic.ObjectEditView):
    queryset = models.ADC.objects.all()
    form = forms.ADCForm


class ADCDeleteView(generic.ObjectDeleteView):
    queryset = models.ADC.objects.all()
