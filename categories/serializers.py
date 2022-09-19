from rest_framework import serializers
from .models import ThirdCategory, FirstCategory, SecondCategory


class ThirdCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdCategory
        fields = ('id', 'name', 'sub_categories')


class SecondCategorySerializer(serializers.ModelSerializer):
    sub_categories = ThirdCategorySerializer(many=True)
    
    class Meta:
        model = SecondCategory
        fields = ('id', 'name', 'sub_categories')


class FirstCategorySerializer(serializers.ModelSerializer):
    sub_cats = SecondCategorySerializer(many=True)

    class Meta:
        model = FirstCategory
        fields = ('id', 'name','sub_cats')
