from .models import ThirdCategory
from rest_framework import viewsets, permissions
from .serializers import ThirdCategorySerializer


class ThirdCategoryViewSet(viewsets.ModelViewSet):
    queryset = ThirdCategory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ThirdCategorySerializer
    