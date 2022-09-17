from rest_framework import routers
from .api import ThirdCategoryViewSet, FirstCategoryViewSet


router = routers.DefaultRouter()
router.register('api/sub_categories', ThirdCategoryViewSet, 'category')

urlpatterns = router.urls
