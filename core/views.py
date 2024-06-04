from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics, permissions
from .models import Observation, Request, User
from .serializers import UserSerializer, ObservationSerializer, RequestSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.authentication import JWTAuthentication



class UserCreateView(generics.CreateAPIView):
    """
    Create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    authentication_classes = []

class UserDetailView(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a user profile.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    authentication_classes = []



class ObservationViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for observations.
    """
    #TODO only Biologist can view ALL obvservation.
    #QUESTION, it does not says but probably citizens can see their own observations
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Biologists').exists():
            return Observation.objects.all()
        return Observation.objects.filter(user=user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assign the authenticated user
    


class RequestViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for requests.
    """
#TODO only Biologist can create request.
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]