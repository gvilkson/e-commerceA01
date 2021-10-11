from django.urls import path

from checkout import views as v

app_name = 'checkout'


urlpatterns = [
    path('', v.checkout, name='checkout'),
]
