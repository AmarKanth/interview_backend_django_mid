from rest_framework.pagination import LimitOffsetPagination

class InventoryPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 100