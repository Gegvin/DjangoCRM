from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, OrderViewSet, StaffViewSet

app_name = "crm"

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'staff', StaffViewSet)

urlpatterns = router.urls