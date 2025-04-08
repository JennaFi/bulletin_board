import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Product, Review

User = get_user_model()


@pytest.fixture
def user():
    """ Creating test user"""

    return User.objects.create_user(email='testuser@django.org', username='testuser', password='password')


@pytest.fixture
def admin_user():
    """Creating test admin user"""

    return User.objects.create_superuser(email='admin@example.com', username='admin', password='adminpassword')


@pytest.fixture
def product(user):
    """Creating product advertisement"""

    return Product.objects.create(name='Test Product', price=5000, owner=user)


@pytest.fixture
def review(product, user):
    """Creating test review"""

    return Review.objects.create(text='Test Review', product=product, owner=user)


@pytest.fixture
def api_client():
    """Test API-client"""

    return APIClient()


@pytest.mark.django_db
def test_create_product(api_client, user):
    """Test product announcement"""

    api_client.force_authenticate(user=user)
    url = reverse('board:product-create')
    data = {'name': 'New Product', 'price': 2000, 'description': 'New Product Description'}

    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'New Product'
    assert response.data['price'] == 2000


@pytest.mark.django_db
def test_get_product_list(api_client, product):
    """Test product list"""

    url = reverse('board:product-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['name'] == product.name


@pytest.mark.django_db
def test_get_product_detail(api_client, product):
    """Test product retrieve"""

    url = reverse('board:product-get', args=[product.id, ], )
    api_client.force_authenticate(user=product.owner)

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == product.name
    assert response.data['price'] == product.price


@pytest.mark.django_db
def test_update_product(product, user, api_client):
    """Test product update"""

    api_client.force_authenticate(user=user)
    url = reverse('board:product-update', args=[product.id])
    data = {'name': 'Updated product announcement', 'price': 3000, 'description': 'Updated Description'}

    response = api_client.put(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Updated product announcement'
    assert response.data['price'] == 3000


@pytest.mark.django_db
def test_delete_product(api_client, product, user):
    """Test product delete"""

    api_client.force_authenticate(user=user)
    url = reverse('board:product-delete', args=[product.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Product.objects.count() == 0


@pytest.mark.django_db
def test_create_review(user, product, api_client):
    """Test creating review"""

    api_client.force_authenticate(user=user)
    url = reverse('board:review-create')
    data = {'text': 'New Review', 'product': product.id}

    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['text'] == 'New Review'
    assert response.data['product'] == product.id


@pytest.mark.django_db
def test_get_review_list(api_client, review, user):
    """Test review list"""

    api_client.force_authenticate(user=user)
    url = reverse('board:review-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['text'] == review.text


@pytest.mark.django_db
def test_get_review_detail(api_client, review, user):
    """Test detail review"""

    api_client.force_authenticate(user=user)
    url = reverse('board:review-get', args=[review.id])

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['text'] == review.text


@pytest.mark.django_db
def test_update_review(api_client, review, user):
    """Test review update"""

    api_client.force_authenticate(user=user)
    url = reverse('board:review-update', args=[review.id])
    data = {'text': 'Updated Review'}

    response = api_client.put(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['text'] == 'Updated Review'


@pytest.mark.django_db
def test_delete_review(api_client, review, user):
    """Test review delete"""

    api_client.force_authenticate(user=user)
    url = reverse('board:review-delete', args=[review.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Review.objects.count() == 0
