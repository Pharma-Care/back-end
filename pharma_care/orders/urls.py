from django.urls import path
from .views import ListCreateOrdersAPIView

# from main.views import
urlpatterns = [
    path("", ListCreateOrdersAPIView.as_view()),
]
