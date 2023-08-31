from rest_framework import routers
from apps.users.api.viewsets import UserViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]