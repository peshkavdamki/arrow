from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers

from .models import *
from .forms import PackForm, CustomForm

# Create your views here.


def landing(request):
    boost_pack = Pack.objects.filter(type='B')
    qual_pack = Pack.objects.filter(type='Q')
    custom = Pack.objects.get(type='C')
    return render(request, 'overwatch/landing.html', locals())


def product_detail(request, id):
    print(request)
    product = get_object_or_404(Pack, id=id, is_active=True)

    if product.type == 'C':
        if request.method != 'POST':
            form = CustomForm()
        else:
            form = CustomForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect('thanks')
    else:
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
        form = CustomForm(request.POST)

        if form.is_valid():
            new_order = form.save(commit=False)

            new_order.type = product.type
            new_order.pack = product.name
            new_order.price = product.price
            new_order.save()


    return render(request, 'overwatch/thanks.html', locals())


def packets(request):
    data = serializers.serialize('json', Pack.objects.filter(is_active=True))
    return HttpResponse(data)
