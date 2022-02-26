from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^v1/products/', include('products.urls', namespace="v1")),
    re_path(r'^v2/products/', include('products.urls', namespace="v2")),
]
