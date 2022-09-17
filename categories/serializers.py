from rest_framework import serializers
from .models import ThirdCategory, FirstCategory


class ThirdCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdCategory
        fields = ('sub_categories', 'id', 'name')

class FirstCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstCategory
        fields = ('id', 'name')
