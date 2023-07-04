from rest_framework.routers import DefaultRouter

from .viewsets import UserViewset, AddressViewset

router = DefaultRouter()
router.register(r"users", UserViewset, basename="users")
router.register(r"addresses", AddressViewset, basename="addresses")
