from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')

    if sort == 'name':
        context = {'phones': Phone.objects.order_by('name')}
    elif sort == 'min_price':
        context = {'phones': Phone.objects.order_by('price')}
    elif sort == 'max_price':
        context = {'phones': Phone.objects.order_by('-price')}
    else:
        context = {'phones': Phone.objects.all()}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.filter(slug=slug)[0]}
    return render(request, template, context)
