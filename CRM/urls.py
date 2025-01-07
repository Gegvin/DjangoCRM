# crm/urls.py

from rest_framework.routers import DefaultRouter
from .views import (
    OrderViewSet,
    StaffViewSet,
    custom_order_list,
    create_order,
    mark_paid,
    delete_order  # Импортируем новое представление
)
from django.urls import path, include

app_name = "crm"

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'staff', StaffViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orderss/', custom_order_list, name='order_list'),
    path('orderss/create/', create_order, name='create_order'),
    path('orderss/<int:order_id>/paid/', mark_paid, name='mark_paid'),
    path('orderss/<int:order_id>/delete/', delete_order, name='delete_order'),  # Новый маршрут
]