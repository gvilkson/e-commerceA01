from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('accounts/', include('accounts.urls')),  # without namespace
    path('admin/', admin.site.urls),
]
