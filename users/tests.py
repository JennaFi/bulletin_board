import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def user():
    """Creation of User"""

    return User.objects.create(
        email='test1@test1.com',
        username='User1',
        password='123qwe456rty',
        first_name='Jane',
        last_name='Doe',

    )


@pytest.fixture
def api_client():
    """Creation of API client"""

    return APIClient()


@pytest.mark.django_db
def test_user_create(api_client, user):
    """Testing creation of user"""

    url = reverse('users:register')

    data = {'email': 'test2@test2.com', 'username': 'new_user', 'first_name': 'Jane', 'last_name': 'Doe',
            'password': '123qwe456rty'}

    response = api_client.post(url, data)

    assert response.status_code, status.HTTP_201_CREATED
    assert User.objects.all().count() == 2


@pytest.mark.django_db
def test_delete_user(api_client, user):
    """Delete user test"""

    api_client.force_authenticate(user=user)

    url = reverse('users:user-delete', args=(user.pk,))

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert User.objects.all().count() == 0
