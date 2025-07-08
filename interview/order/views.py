from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from django.shortcuts import render, get_object_or_404

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DeactivateOrderView(APIView):
    def patch(self, request: Request, pk: int, *args, **kwargs) -> Response:
        order = get_object_or_404(Order, id=pk)
        order.is_active = False
        order.save()
        return Response({"message": f"Order {pk} has been deactivated."}, status=status.HTTP_200_OK)


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer
