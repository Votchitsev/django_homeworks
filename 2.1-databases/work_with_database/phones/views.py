from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


SORT_MAP = {
    'name': 'name',
    'min_price': 'price',
    'max_price': '-price'
}


def index(request):
    return redirect('catalog')


def show_catalog(request):

    template = 'catalog.html'
    sort = request.GET.get('sort')

    if sort:
        context = {'phones': Phone.objects.order_by(SORT_MAP[sort])}
        return render(request, template, context)
    else:
        context = {'phones': Phone.objects.order_by('name')}
        return render(request, template, context)


def show_product(request, slug):

    template = 'product.html'

    try:
        context = {'phone': Phone.objects.filter(slug=slug)[0]}
        return render(request, template, context)
    except IndexError as error:
        print(error)
        return HttpResponse(f"ОШИБКА: {error}")
