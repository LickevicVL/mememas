from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory, Client

from memes.views import CreateMem


class MemTestCase(TestCase):
    def setUp(self):
        factory = RequestFactory()
        self.request = factory.post('/memes/create/', data={
            'title': 'TestMem',
            'body': 'TestBody',
            'image': 'Image'.encode()
        })
        self.view = CreateMem.as_view()
        self.client = Client()

    def test_create_mem_with_unknown_user(self):
        response = self.client.post('/memes/create/')
        self.assertEqual(response.status_code, 403)

    def test_create_mem_with_specific_user(self):
        user = User.objects.create_superuser(
            username='mememas', password='123', email=None
        )
        user.save()

        self.request.user = user
        response = self.view(self.request)
        self.assertEqual(response.status_code, 200)
