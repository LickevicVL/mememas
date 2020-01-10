from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.serializers import MemSerializer
from memes.models import Mem


class MemApi(ListAPIView, CreateAPIView):
    queryset = Mem.objects.all()
    serializer_class = MemSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
