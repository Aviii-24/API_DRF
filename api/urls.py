from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WheelSpecificationViewSet, BogieChecksheetViewSet

router = DefaultRouter()
router.register(r'wheelspecs', WheelSpecificationViewSet)
router.register(r'bogiechecks', BogieChecksheetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]