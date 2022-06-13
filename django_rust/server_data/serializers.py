from rest_framework.serializers import ModelSerializer

from server_data.models import Player, Server


class ServerSerializer(ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'

    
class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
