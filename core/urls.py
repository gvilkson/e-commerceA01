from django.urls import path

from core import views as v

app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
    path('contact/', v.contact, name='contact'),
]
