from django.db.models import Q
from rest_framework.filters import SearchFilter, BaseFilterBackend
from rest_framework.viewsets import ModelViewSet

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['$title', 'description']


class StockViewFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        try:
            product_title = request.GET['products']
            product_title = product_title.capitalize()
            print('Yes')
            return queryset.filter(
                Q(products__title__icontains=product_title) |
                Q(products__description__icontains=product_title)
            ).order_by('id')
        except KeyError:
            return queryset


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all().order_by('id')
    serializer_class = StockSerializer
    filter_backends = [StockViewFilter]
    filterset_fields = ['products']
