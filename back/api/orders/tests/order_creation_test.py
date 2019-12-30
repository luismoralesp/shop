from rest_framework import status
from django.test import TestCase
from django.test import Client
from ..constants import OrderStatus
import json

class OrderCreationTest(TestCase):
    """ class to test order API """

    def test_create_order(self):
        c = Client()

        client_data = {
            "name": "Deion",
            "surname": "Ondricka",
            "email": "dnetix@yopmail.com",
            "document": "1040035000",
            "documentType": "CC",
            "mobile": "3006108300"
        }
        response = c.post('/api/orders/', client_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        json_content = json.loads(response.content)

        self.assertTrue( client_data.items() <= json_content['client'].items())
        self.assertEqual(json_content['status'], OrderStatus.CREATED)
        
    def test_create_order_documentType_wrong(self):
        c = Client()

        client_data = {
            "name": "Deion",
            "surname": "Ondricka",
            "email": "dnetix@yopmail.com",
            "document": "1040035000",
            "documentType": "CX",
            "mobile": "3006108300"
        }
        response = c.post('/api/orders/', client_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_order_email_wrong(self):
        c = Client()

        client_data = {
            "name": "Deion",
            "surname": "Ondricka",
            "email": "dnetix$yopmail.com",
            "document": "1040035000",
            "documentType": "CX",
            "mobile": "3006108300"
        }
        response = c.post('/api/orders/', client_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        
        
