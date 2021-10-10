from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views as v

# Read https://github.com/rg3915/django-auth-tutorial
'''
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
'''

urlpatterns = [
    path('login/', v.login, name='login'),
    path('logout/', v.logout, name='logout'),
]