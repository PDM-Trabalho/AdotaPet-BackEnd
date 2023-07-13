from rest_framework.routers import DefaultRouter

from .viewsets import UserViewset, AddressViewset, ProfileViewset

router = DefaultRouter()
router.register(r"users", UserViewset, basename="users")
router.register(r"profiles", ProfileViewset, basename="users")
router.register(r"addresses", AddressViewset, basename="addresses")
