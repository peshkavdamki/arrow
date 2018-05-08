from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import *
from .forms import PackForm

# Create your views here.


def landing(request):
    boost_pack = Pack.objects.filter(type='B')
    qual_pack = Pack.objects.filter(type='Q')
    return render(request, 'overwatch/landing.html', locals())


def product_detail(request, id):
    print(request)
    product = get_object_or_404(Pack, id=id, is_active=True)

    if request.method != 'POST':
        form = PackForm()
    else:
        form = PackForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('thanks')

    context = {
        'product': product,
        'form': form
    }
    return render(request, 'overwatch/pack_detail.html', context)


def thanks(request, id):
    product = Pack.objects.get(id=id)
    if request.method == 'POST':
        print(product)
        print(id)
        form = PackForm(request.POST)

        if form.is_valid():
            new_order = form.save(commit=False)

            new_order.type = product.type
            new_order.pack = product.name
            new_order.price = product.price
            new_order.save()


    return render(request, 'overwatch/landing.html', locals())
