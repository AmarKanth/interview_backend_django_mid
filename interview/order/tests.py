from datetime import date, timedelta
from rest_framework import status

from interview.tests.api_request_factory import APIViewRequestFactory
from interview.order.views import OrderListCreateView, DeactivateOrderView
from interview.order.serializers import OrderSerializer
from interview.order.models import Order


class TestOrderListCreateView(APIViewRequestFactory):
    view_name = OrderListCreateView

    def test_orders_list(self):
        response = self.send_request_to_view(method="get")
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_orders_list_with_valid_dates(self):
        start = date.today().isoformat()
        end = (date.today() + timedelta(days=7)).isoformat()
        query_params = {"start": start, "end": end}

        response = self.send_request_to_view(method="get", query_params=query_params)

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_orders_list_with_invalid_dates(self):
        start = date.today().isoformat()
        end = (date.today() + timedelta(days=7)).isoformat()
        query_params = {"start": start, "end": end}

        response = self.send_request_to_view(method="get", query_params=query_params)

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestDeactivateOrderView(APIViewRequestFactory):
    view_name = DeactivateOrderView

    def test_deactivate_order(self):
        order = Order.objects.first()
        path_params = {"pk": order.id}
        expected_response = {"message": f"Order {order.id} has been deactivated."}

        response = self.send_request_to_view(method="patch", path_params=path_params)

        self.assertEqual(response.data, expected_response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deactivate_order_with_invalid_id(self):
        path_params = {"pk": 10000}
        response = self.send_request_to_view(method="patch", path_params=path_params)

        self.assertEqual(response.data["detail"], "Not found.")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
