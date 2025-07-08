from urllib.parse import urlencode
from django.test import TestCase
from rest_framework.test import APIRequestFactory

from interview.inventory.models import (
    Inventory,
    InventoryType,
    InventoryLanguage,
    InventoryTag,
)


class APIViewRequestFactory(TestCase):
    view_name = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        _type = InventoryType.objects.create(name="Movie")
        language = InventoryLanguage.objects.create(name="English")
        tag = InventoryTag.objects.create(name="Action", is_active=True)

        inventory = Inventory.objects.create(
            name="The Matrix",
            type=_type,
            language=language,
            metadata={
                "year": 1999,
                "actors": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
                "imdb_rating": 8.7,
                "rotten_tomatoes_rating": 87,
            },
        )
        inventory.tags.add(tag)

    @classmethod
    def tearDownClass(cls):
        Inventory.objects.all().delete()
        InventoryTag.objects.all().delete()
        InventoryType.objects.all().delete()
        InventoryLanguage.objects.all().delete()
        super().tearDownClass()

    def send_request_to_view(self, method, path_params=None, query_params=None, data=None):
        path_params = path_params or {}
        query_params = query_params or {}

        factory = APIRequestFactory()
        view = self.view_name.as_view()

        query_string = urlencode(query_params)
        url = f"/fake_url/?{query_string}" if query_string else "/fake_url/"

        request = getattr(factory, method.lower())(url, data)
        request.query_params = query_params
        response = view(request, **path_params)
        return response
