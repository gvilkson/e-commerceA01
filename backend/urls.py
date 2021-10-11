from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls', namespace='blog')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('accounts/', include('accounts.urls')),  # without namespace
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
]
