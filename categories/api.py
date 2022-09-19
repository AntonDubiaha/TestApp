from .models import ThirdCategory, FirstCategory, SecondCategory
from rest_framework import viewsets, permissions
from .serializers import ThirdCategorySerializer, FirstCategorySerializer, SecondCategorySerializer


class FirstCategoryViewSet(viewsets.ModelViewSet):
    queryset = FirstCategory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FirstCategorySerializer

class ThirdCategoryViewSet(viewsets.ModelViewSet):
    queryset = ThirdCategory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ThirdCategorySerializer


class SecondCategoryViewSet(viewsets.ModelViewSet):
    queryset = SecondCategory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SecondCategorySerializer

    