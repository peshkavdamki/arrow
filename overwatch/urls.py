from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^(?P<id>\d+)/', views.product_detail, name='product_detail'),
    url(r'^thanks/(?P<id>\d+)/', views.thanks, name='thanks')
]
