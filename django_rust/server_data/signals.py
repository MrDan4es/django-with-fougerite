from django.dispatch import receiver    
from django.db.models.signals import post_save,post_delete
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from server_data.models import Server


channel_layer = get_channel_layer()

@receiver(post_save, sender=Server)
def create_room_signal(sender, instance, created, *args, **kwargs):
    async_to_sync(channel_layer.group_send)(
    'main',
        {
            'type': 'websocket_server',
            'online': instance.is_on
        }
    )
