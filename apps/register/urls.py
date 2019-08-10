from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.signup),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^buyTrans$', views.buying_transaction),
    url(r'^sellTrans$', views.selling_transaction)
]