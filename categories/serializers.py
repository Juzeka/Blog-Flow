from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(CategorySerializer):
    class Meta(CategorySerializer.Meta):
        fields = ['id', 'name']
