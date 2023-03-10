from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "user", "products"]

    def create(self, validated_data):
        return Cart.objects.create(**validated_data)