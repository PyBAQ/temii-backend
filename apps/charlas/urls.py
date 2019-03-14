from rest_framework.routers import DefaultRouter
from .viewsets import CharlaViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('talks', CharlaViewSet)

urlpatterns = router.get_urls()