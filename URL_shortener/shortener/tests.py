from rest_framework.test import APITestCase
from rest_framework import status

class UrlShortenerTests(APITestCase):
    def test_create_shortened_url(self):
        response = self.client.post('/api/shortener/create', {'original_url': 'https://example.com'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('shortened_url', response.data)

    def test_redirect_to_original_url(self):
        response = self.client.post('/api/shortener/create', {'original_url': 'https://example.com'})
        shortened_url = response.data['shortened_url']

        response = self.client.get(f'/api/shortener/{shortened_url}/')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.data['original_url'], 'https://example.com')
