from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, get_user_model


class UserViewset(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
