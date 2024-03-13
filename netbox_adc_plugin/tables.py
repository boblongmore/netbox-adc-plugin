import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn

from .models import ADC


class ADCTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = ADC
        fields = ("pk", "id", "name", "actions")
        default_columns = ("name",)
