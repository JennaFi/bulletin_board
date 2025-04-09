from rest_framework import serializers

from board.models import Review, Product


class ReviewSerializer(serializers.ModelSerializer):
    """Review serializer"""

    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Product serializer"""

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        exclude = ('slug',)
