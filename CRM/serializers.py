from rest_framework import serializers
from .models import Order, Staff

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'order_number',
            'coffee',
            'syrup',
            'status',
            'created_at',
            'coffee_price',
            'syrup_price',
            'total_price',
        ]
        read_only_fields = [
            'order_number',
            'created_at',
            'coffee_price',
            'syrup_price',
            'total_price',
        ]

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'name', 'email']