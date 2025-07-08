from django.urls import path
from interview.order.views import (
    OrderListCreateView,
    OrderTagListCreateView,
    DeactivateOrderView,
    OrderTagsView
)


urlpatterns = [
    path("tags/", OrderTagListCreateView.as_view(), name="order-detail"),
    path("", OrderListCreateView.as_view(), name="order-list"),
    path("<int:pk>/deactivate/", DeactivateOrderView.as_view(), name="deactivate-order"),
    path('<int:pk>/tags/', OrderTagsView.as_view(), name='order-tags'),
]
