from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from board.models import Product, Review
from board.pagination import ProductPaginator
from board.serializers import ProductSerializer, ReviewSerializer
from users.permissions import IsAdmin, IsAuthor


class ProductCreateAPIView(generics.CreateAPIView):
    """Creation of announcement, only for authenticated users"""

    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        product = serializer.save()
        product.owner = self.request.user
        product.save()


class ProductListAPIView(generics.ListAPIView):
    """List of all announcements"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    pagination_class = ProductPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('name',)
    ordering_fields = ('created_at',)


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """Retrieve specific announcement"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsAuthor]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """Update specific announcement"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsAuthor]


class ProductDestroyAPIView(generics.DestroyAPIView):
    """Delete specific announcement"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsAuthor]


class ReviewCreateAPIView(generics.CreateAPIView):
    """Creation of review for announcement, only for authenticated users"""

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        review = serializer.save()
        review.author = self.request.user
        review.save()


class ReviewListAPIView(generics.ListAPIView):
    """List of all reviews for specific announcement"""

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated, ]


class ReviewRetrieveAPIView(generics.RetrieveAPIView):
    """Retrieve specific review for announcement"""

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsAuthor]


class ReviewUpdateAPIView(generics.UpdateAPIView):
    """Update specific review for announcement"""

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsAuthor]


class ReviewDestroyAPIView(generics.DestroyAPIView):
    """Delete specific review for announcement"""

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsAuthor]
