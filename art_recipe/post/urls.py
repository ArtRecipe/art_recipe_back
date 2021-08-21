from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register("post", views.PostViewSet)
router.register("material", views.MaterialViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("image/", views.PostImageView.as_view()),
]