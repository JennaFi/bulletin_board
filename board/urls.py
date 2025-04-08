from django.urls import path

from board.apps import BoardConfig
from board.views import ProductCreateAPIView, ProductListAPIView, ProductRetrieveAPIView, ProductUpdateAPIView, \
    ProductDestroyAPIView, ReviewCreateAPIView, ReviewListAPIView, ReviewRetrieveAPIView, ReviewUpdateAPIView, \
    ReviewDestroyAPIView

app_name = BoardConfig.name

urlpatterns = [
    path('product/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('product/', ProductListAPIView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-get'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('product/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product-delete'),
    path('review/create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('review/', ReviewListAPIView.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewRetrieveAPIView.as_view(), name='review-get'),
    path('review/update/<int:pk>/', ReviewUpdateAPIView.as_view(), name='review-update'),
    path('review/delete/<int:pk>/', ReviewDestroyAPIView.as_view(), name='review-delete'),
]
