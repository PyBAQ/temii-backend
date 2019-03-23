from django_filters import rest_framework as filters

from .models import CharlaModel

class CharlaFilter(filters.FilterSet):
    class Meta:
        model = CharlaModel
        fields = ['estado']