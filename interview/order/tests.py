from rest_framework import status

from interview.tests.api_request_factory import APIViewRequestFactory
from interview.order.views import DeactivateOrderView

from interview.order.models import Order


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
