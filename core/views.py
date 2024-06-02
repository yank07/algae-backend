from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics
from .models import Observation, Request, User
from .serializers import UserSerializer, ObservationSerializer, RequestSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserCreateView(generics.CreateAPIView):
    """
    Create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a user profile.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ObservationViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for observations.
    """
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer

class RequestViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for requests.
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    
    @swagger_auto_schema(
        operation_description="Get a list of all requests",
        responses={200: RequestSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        """
        List all requests.
        """
        return super().list(request, *args, **kwargs)