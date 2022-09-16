from rest_framework import routers
from .api import ThirdCategoryViewSet


router = routers.DefaultRouter()
router.register('api/sub_categories', ThirdCategoryViewSet, 'categories')

urlpatterns = router.urls
