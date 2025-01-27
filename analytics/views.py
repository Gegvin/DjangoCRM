# analytics/views.py

from django.shortcuts import render
from .utils import get_orders
from .models import OrderAnalytics
from django.contrib.auth.decorators import login_required
import pandas as pd
from decimal import Decimal, InvalidOperation
import logging

logger = logging.getLogger(__name__)

@login_required
def dashboard(request):
    orders_data = get_orders()
    if orders_data:
        # Преобразуем 'total_price', 'coffee_price' и 'syrup_price' из строки в Decimal
        for order in orders_data:
            try:
                order['total_price'] = Decimal(order['total_price'])
                order['coffee_price'] = Decimal(order['coffee_price'])
                order['syrup_price'] = Decimal(order['syrup_price'])
            except InvalidOperation as e:
                logger.error(f"Ошибка преобразования данных заказа: {order}, ошибка: {e}")
                order['total_price'] = Decimal('0.00')
                order['coffee_price'] = Decimal('0.00')
                order['syrup_price'] = Decimal('0.00')

        # аналитики: общее количество заказов и общий доход
        total_orders = len(orders_data)
        total_revenue = sum(order['total_price'] for order in orders_data)

        # Дополнительная аналитика с использованием pandas
        df = pd.DataFrame(orders_data)
        # Преобразуем 'total_price', 'coffee_price' и 'syrup_price' в float для pandas
        df['total_price'] = df['total_price'].astype(float)
        df['coffee_price'] = df['coffee_price'].astype(float)
        df['syrup_price'] = df['syrup_price'].astype(float)

        revenue_by_coffee = df.groupby('coffee')['total_price'].sum().to_dict()
        revenue_by_syrup = df.groupby('syrup')['total_price'].sum().to_dict()

        # Отладочные выводы
        print("Revenue by coffee:", revenue_by_coffee)
        print("Revenue by syrup:", revenue_by_syrup)

        context = {
            'total_orders': total_orders,
            'total_revenue': total_revenue,
            'revenue_by_coffee': revenue_by_coffee,
            'revenue_by_syrup': revenue_by_syrup,
        }
    else:
        context = {
            'error': 'Не удалось получить данные из API.',
        }

    return render(request, 'analytics/dashboard.html', context)