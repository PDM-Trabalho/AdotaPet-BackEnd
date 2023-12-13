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

from rest_framework.decorators import action
from rest_framework.response import Response


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

    @action(
        detail=False,
        methods=["GET"],
        serializer_class=UserSerializer,
    )
    def me(self, request):
        user = self.request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class ProfileViewset(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
