from urllib import response
from django.test import TestCase
from requests import request
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import RequestsClient
from grocery import views

# Create your tests here.



client = RequestsClient()

response = client.get('http://127.0.0.1:9000/api/products/')
assert response.status_code == 200

# class TestProduct(APITestCase):

#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.view = views.product_list()
#         self.uri = '/products/'

#     def test_list(self):
#         request = self.factory.get(self.uri)
#         response = self.view(request)
#         self.assertEqual(response.status_code, 200, 'Expected Response Code 200, recieved {0} Instead.'.format(response.status_code) )




