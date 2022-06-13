from rest_framework import viewsets

from server_data.serializers import ServerSerializer, PlayerSerializer
from server_data.models import Server, Player

    
class ServerViewSet(viewsets.ModelViewSet):
    serializer_class = ServerSerializer
    queryset = Server.objects.all()


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    lookup_field = 'steam_ID'
    