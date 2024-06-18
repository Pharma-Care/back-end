from django.urls import path
from .views import CommonUserEndpoint, ListCreateUsersAPIView

# from main.views import
urlpatterns = [
    path("users/me/", CommonUserEndpoint.as_view(), name="get-common-user"),
    path("users/", ListCreateUsersAPIView.as_view(), name="list-create-users"),
]
