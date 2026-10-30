from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, VehicleViewSet

# 自动生成API路由
router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'vehicles', VehicleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
]
