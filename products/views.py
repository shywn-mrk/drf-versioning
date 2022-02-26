from rest_framework import generics
from .models import Product
from .serializers import ProductSerializerV1, ProductSerializerV2

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return ProductSerializerV1
        return ProductSerializerV2
