from rest_framework import viewsets
from rest_framework.response import Response
from django.http import Http404

from server_data.serializers import ServerSerializer, PlayerSerializer
from server_data.models import Server, Player

    
class ServerViewSet(viewsets.ModelViewSet):
    serializer_class = ServerSerializer
    queryset = Server.objects.all()


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    lookup_field = 'steam_ID'

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response(kwargs.get('steam_ID'), 234) # custom 404 code, callback doesn't work on 404 
        return Response(kwargs.get('steam_ID'), 200)
