from django.urls import path
from .views import CommonUserEndpoint

# from main.views import
urlpatterns = [path("users/me/", CommonUserEndpoint.as_view(), name="get-common-user")]
