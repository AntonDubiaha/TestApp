from .models import ThirdCategory, FirstCategory
from rest_framework import viewsets, permissions
from .serializers import ThirdCategorySerializer, FirstCategorySerializer


class ThirdCategoryViewSet(viewsets.ModelViewSet):
    queryset = ThirdCategory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ThirdCategorySerializer
    
class FirstCategoryViewSet(viewsets.ModelViewSet):
    queryset = FirstCategory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FirstCategorySerializer
    