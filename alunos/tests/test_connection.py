from django.test import TestCase, Client
from django.urls import reverse


class BasicConnectionTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse('index:index')

    def test_index_loads_properly(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
