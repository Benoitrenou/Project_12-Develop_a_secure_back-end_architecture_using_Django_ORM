from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from events.models import Event
from events.permissions import HasEventPermissions
from events.serializers import EventSerializer


class EventViewSet(ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        IsAuthenticated,
        HasEventPermissions
        ]
    filterset_fields = [
        'contract__client__company__sales_contact',
        'support_contact',
        'finsihed',
        'attendees',
        'date',
        ]
