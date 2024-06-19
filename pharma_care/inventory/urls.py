from rest_framework import routers
from . import views
from django.urls import path

router = routers.DefaultRouter()

router.register(r"", views.InventoryItemViewSet, basename="inventory")
urlpatterns = [
    path(
        "patch/<int:pk>/",
        views.UpdateDestroyItemView.as_view(),
        name="update-inventory",
    ),
]

urlpatterns += router.urls
