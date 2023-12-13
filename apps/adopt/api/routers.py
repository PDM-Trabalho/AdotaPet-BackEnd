from rest_framework.routers import DefaultRouter

from .viewsets import PetViewset, PictureViewset

router = DefaultRouter()
router.register(r"pets", PetViewset, basename="pets")
router.register(r"pictures", PictureViewset, basename="pictures")
