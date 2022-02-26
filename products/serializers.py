from rest_framework import serializers
from .models import Product


class ProductSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title']
