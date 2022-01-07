import django_filters
from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = django_filters.DateFromToRangeFilter()
    status = django_filters.CharFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
