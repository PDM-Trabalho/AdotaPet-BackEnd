from rest_framework.routers import DefaultRouter

from .viewsets import PetViewset

router = DefaultRouter()
router.register(r"pets", PetViewset, basename="pets")
