from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Trip
from .serializers import UserSerializer, LogInSerializer, TripSerializer


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LogInView(TokenObtainPairView): # new
    serializer_class = LogInSerializer


class TripView(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id' # new
    lookup_url_kwarg = 'trip_id' # new
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

