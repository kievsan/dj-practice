from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    sort = request.GET.get('sort', 'name')  # по умолчанию: сортировка по названию

    # по дороговизне и по названию
    if sort == 'min_price':
        prods = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        prods = Phone.objects.all().order_by('-price')
    else:
        prods = Phone.objects.all().order_by(sort)

    context = {"phones": prods}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    prod = Phone.objects.filter(slug=slug)[0]
    context = {"phone": prod}
    return render(request, template, context)
