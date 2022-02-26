from django.urls import re_path
from .views import ProductView


app_name = 'products'

urlpatterns = [
    re_path(r'^$', ProductView.as_view(), name='products'),
]
