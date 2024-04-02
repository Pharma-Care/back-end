from rest_framework import routers
from . import views
router = routers.DefaultRouter()

router.register(r'', views.InventoryItemViewSet, basename='inventory')
urlpatterns = []

urlpatterns = router.urls