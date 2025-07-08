from datetime import date, timedelta
from rest_framework import status

from interview.tests.api_request_factory import APIViewRequestFactory
from interview.inventory.views import InventoryListCreateView
from interview.inventory.serializers import InventorySerializer
from interview.inventory.models import Inventory


class TestInventoryListCreateView(APIViewRequestFactory):
    view_name = InventoryListCreateView

    def test_list_of_inventories(self):
        response = self.send_request_to_view(method="get")
        inventories = Inventory.objects.all()[:3]
        serializer = InventorySerializer(inventories, many=True)

        self.assertIn("count", response.data)
        self.assertIn("next", response.data)
        self.assertIn("previous", response.data)
        self.assertIn("results", response.data)

        self.assertEqual(response.data["results"], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_of_inventories_with_date_filter(self):
        created_after_date = (date.today() - timedelta(days=10)).isoformat()
        query_params = {"created_after": created_after_date}

        response = self.send_request_to_view(method="get", query_params=query_params)
        inventories = Inventory.objects.filter(created_at__gt=created_after_date)[:3]
        serializer = InventorySerializer(inventories, many=True)

        self.assertEqual(response.data["results"], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_of_inventories_with_invalid_date(self):
        query_params = {"created_after": "13131/2131/131"}
        response = self.send_request_to_view(method="get", query_params=query_params)
        self.assertEqual(response.data["results"], [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
