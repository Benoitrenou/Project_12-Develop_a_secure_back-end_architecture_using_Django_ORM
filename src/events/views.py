from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from events.models import Event
from events.serializers import EventSerializer


class EventViewSet(ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
