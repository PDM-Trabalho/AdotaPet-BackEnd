from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .serializers import PetSerializer
from ..models import Pet


class PetViewset(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def perform_create(self, serializer):
        serializer.save(donatario=self.request.user)

    @action(detail=True, methods=["post"])
    def adopt(self, request, pk=None):
        pet = self.get_object()

        logged_user = request.user

        if pet.donatario.id == logged_user.id:
            return Response(
                {"error": "Cannot adopt your own pet."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        pet.adotante = logged_user
        pet.save()

        return Response(
            {"message": "Pet adopted successfully."}, status=status.HTTP_200_OK
        )
