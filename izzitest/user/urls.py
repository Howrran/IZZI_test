"""
User urls
"""
from django.urls import include, path
from rest_framework import routers

from .view import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls), name='all_users'),
]
