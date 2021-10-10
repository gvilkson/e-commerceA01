from django.urls import path

from blog import views as v

app_name = 'blog'


urlpatterns = [
    path('', v.blog, name='blog'),
]
