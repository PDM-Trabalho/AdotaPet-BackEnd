from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, get_user_model, AddressSerializer, Address


class AddressViewset(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class UserViewset(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
