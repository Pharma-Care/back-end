from django.urls import path
from main.views import CommonUserEndpoint

# from main.views import
urlpatterns = [path("users/me/", CommonUserEndpoint.as_view(), name="get-common-user")]
