from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import *


class CreateProviderTest(APITestCase):
    def setUp(self):
        self.data = {
            "name":"test",
            "email":"test@test1.com",
            "phone_number":"9944545445",
            "language":"english",
            "currency":"usd"
        }

    def test_can_create_provider(self):
        response = self.client.post('/api/providers/', self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadProviderTest(APITestCase):
    def setUp(self):
        self.data = {
            "name":"test",
            "email":"test@test1.com",
            "phone_number":"9944545445",
            "language":"english",
            "currency":"usd"
        }
        self.provider = ProviderModel.objects.create(**self.data)

    def test_can_read_provider_list(self):
        response = self.client.get('/api/providers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_provider_detail(self):
        response = self.client.get('/api/providers/' + str(self.provider.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateServiceTest(APITestCase):
    def setUp(self):
        self.data = {
            "provider_id":3,
            "name":"asdf",
            "price":344,
            "geojson":{ "type": "Polygon", "coordinates": [ [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ]]},
            "information":"asdfsfsdf"
        }

    def test_can_create_provider(self):
        response = self.client.post('/api/service_area/', self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadServiceTest(APITestCase):
    def setUp(self):
        self.data = {
            "service_id":1,
            "provider_id":3,
            "name":"asdf",
            "price":344,
            "geojson":{ "type": "Polygon", "coordinates": [ [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ]]},
            "information":"asdfsfsdf"
        }
        self.provider = ServiceModel.objects.create(**self.data)

    def test_can_read_provider_list(self):
        response = self.client.get('/api/service_area/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_provider_detail(self):
        response = self.client.get('/api/service_area/' + str(self.provider.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
