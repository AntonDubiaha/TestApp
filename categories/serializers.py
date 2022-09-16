from rest_framework import serializers
from .models import ThirdCategory


class ThirdCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdCategory
        fields = ('id', 'name')
