from django_property_filter import PropertyFilterSet, PropertyNumberFilter

from map.models import Arc


class ArcFilterSet(PropertyFilterSet):
    level = PropertyNumberFilter(field_name='level', lookup_expr='exact')

    class Meta:
        model = Arc
        fields = ['level']
