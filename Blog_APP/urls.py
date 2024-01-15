from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BlogViewSet

router_blog = DefaultRouter()
router_users = DefaultRouter()

router_users.register(r'', UserViewSet, basename='user')
router_blog.register(r'', BlogViewSet, basename='blog')

urlpatterns = [
    path('users/', include(router_users.urls)),
    path('blogs/', include(router_blog.urls)),
]
