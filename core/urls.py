from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCreateView, UserDetailView, ObservationViewSet, RequestViewSet


router = DefaultRouter()
router.register(r'observations', ObservationViewSet)
router.register(r'requests', RequestViewSet)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
]

urlpatterns += router.urls