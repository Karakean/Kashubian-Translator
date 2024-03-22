from django.test import TestCase

class BackendTests(TestCase):
    def test_get_authors(self):
        response = self.client.get('/api/authors')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), "Filip Szweda, Jakub Grzybowski, Julia Żęgota, Kamil Czepiel, Krzysztof Kulpiński, Michał Wrzosek, Mikołaj Nowak")