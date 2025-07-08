from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from django.shortcuts import render, get_object_or_404
from django.utils.dateparse import parse_date

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()

        start = parse_date(self.request.query_params.get("start", ""))
        end = parse_date(self.request.query_params.get("end", ""))

        if not start and not end:
            return queryset

        if not start or not end:
            return queryset.none()

        return queryset.filter(start_date__gte=start, embargo_date__lte=end)


class DeactivateOrderView(APIView):
    def patch(self, request: Request, pk: int, *args, **kwargs) -> Response:
        order = get_object_or_404(Order, id=pk)
        order.is_active = False
        order.save()
        return Response({"message": f"Order {pk} has been deactivated."}, status=status.HTTP_200_OK)


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrderTagsView(APIView):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        tags = order.tags.all()
        serializer = OrderTagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)