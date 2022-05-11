from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register("post", views.PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]