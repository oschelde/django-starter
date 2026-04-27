from django.urls import path

from .views import (
    UserPageView,
    ProfilePageView,
)

urlpatterns = [
    path("profile/", ProfilePageView.as_view(), name="profile"),
    path("", UserPageView.as_view(), name="user"),
]
