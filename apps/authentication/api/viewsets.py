from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import (
    UserSerializer,
    get_user_model,
    AddressSerializer,
    Address,
    ProfileSerializer,
    Profile,
)


class AddressViewset(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class UserViewset(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.AllowAny()]
        return super().get_permissions()


class ProfileViewset(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
