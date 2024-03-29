from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import ADC


class ADCForm(NetBoxModelForm):
    class Meta:
        model = ADC
        fields = ("name", "tags")
