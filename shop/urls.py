from django.urls import path

from shop import views as v

app_name = 'shop'


urlpatterns = [
    path('', v.shop, name='shop'),
    path('cart/', v.cart, name='cart'),
]
