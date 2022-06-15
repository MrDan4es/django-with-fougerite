from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.response import Response

from server_data.models import ChatMessage, Player, Server


class ServerSerializer(ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'

    
class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class PlayerNicknameSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['nickname']


class ChatMessageSerializer(ModelSerializer):
    player = CharField()

    class Meta:
        model = ChatMessage
        fields = '__all__'

    def create(self, validated_data):
        player = validated_data.pop('player')
        player_instance = Player.objects.get(nickname=player)
        return ChatMessage.objects.create(**validated_data, player=player_instance)
