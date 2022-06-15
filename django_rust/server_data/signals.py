from django.dispatch import receiver    
from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from server_data.models import ChatMessage, Server, Player


MAX_MESSAGES = 100
channel_layer = get_channel_layer()

@receiver(post_save, sender=Server)
def server_signal(sender, instance, created, *args, **kwargs):
    async_to_sync(channel_layer.group_send)(
    'main',
        {
            'type': 'websocket_server',
            'command': 'server',
            'online': instance.is_on
        }
    )

@receiver(post_save, sender=Player)
def player_signal(sender, instance, created, *args, **kwargs):
    async_to_sync(channel_layer.group_send)(
    'main',
        {
            'type': 'websocket_player',
            'command': 'player',
            'nickname': instance.nickname,
            'on_server': instance.on_server
        }
    )

@receiver(post_save, sender=ChatMessage)
def chat_signal(sender, instance, created, *args, **kwargs):
    if ChatMessage.objects.count() > MAX_MESSAGES:
        ids = ChatMessage.objects.order_by("-pk").values_list("pk", flat=True)[:MAX_MESSAGES]
        ChatMessage.objects.exclude(pk__in=list(ids)).delete()
        
    async_to_sync(channel_layer.group_send)(
    'main',
        {
            'type': 'websocket_chat',
            'command': 'chat',
            'nickname': instance.player.nickname,
            'create_date': instance.create_date.isoformat(),
            'text': instance.text
        }
    )
