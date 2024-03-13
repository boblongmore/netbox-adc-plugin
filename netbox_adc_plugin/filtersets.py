from netbox.filtersets import NetBoxModelFilterSet
from .models import ADC


# class ADCFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = ADC
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
