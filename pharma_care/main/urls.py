from django.urls import path
from .views import CommonUserEndpoint, ListCreateUsersAPIView, UpdateDestroyUsersAPIView

# from main.views import
urlpatterns = [
    path("users/me/", CommonUserEndpoint.as_view(), name="get-common-user"),
    path("users/", ListCreateUsersAPIView.as_view(), name="list-create-users"),
    path("users/<int:pk>/", UpdateDestroyUsersAPIView.as_view(), name="update-users"),
]
