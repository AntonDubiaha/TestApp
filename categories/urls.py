from rest_framework import routers
from .api import ThirdCategoryViewSet, FirstCategoryViewSet


router = routers.DefaultRouter()


router.register(r'api/categories', FirstCategoryViewSet, 'categories')
router.register(r'api/sub_categories', ThirdCategoryViewSet, 'sub_categories')

urlpatterns = router.urls
