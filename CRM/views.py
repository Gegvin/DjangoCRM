from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, permissions
from .models import Order, Staff
from .serializers import OrderSerializer, StaffSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Пример настройки разрешений

    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        if order.status:
            return Response({"error": "Нельзя удалить оплаченный заказ."}, status=400)
        return super().destroy(request, *args, **kwargs)
class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

def custom_order_list(request):
    unpaid_orders = Order.objects.filter(status=False)
    paid_orders = Order.objects.filter(status=True)
    return render(request, 'custom_order_list.html', {
        'unpaid_orders': unpaid_orders,
        'paid_orders': paid_orders,
    })

def create_order(request):
    if request.method == 'POST':
        coffee = request.POST.get('coffee')
        syrup = request.POST.get('syrup')
        Order.objects.create(coffee=coffee, syrup=syrup)
        return redirect('crm:order_list')

    # Получаем выборы из модели Order
    coffee_choices = Order.COFFEE_CHOICES
    syrup_choices = Order.SYRUP_CHOICES
    return render(request, 'create_order.html', {
        'coffee_choices': coffee_choices,
        'syrup_choices': syrup_choices,
    })
def mark_paid(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = True
    order.save()
    return redirect('crm:order_list')

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, status=False)  # Убедимся, что заказ не оплачен
    if request.method == 'POST':
        order.delete()
        return redirect('crm:order_list')
    return render(request, 'delete_order_confirm.html', {'order': order})