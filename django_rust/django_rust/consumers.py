from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async

from server_data.models import Server


class MainConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add('main', self.channel_name)

        is_online = await self.is_server_online()
        
        await self.send_json(
            {
                'online': is_online
            }
        )

    async def websocket_server(self, event):
        await self.send_json(
            {
                'online': event['online']
            }
        )
        
    @database_sync_to_async
    def is_server_online(self) -> bool:
        return Server.objects.get(pk=1).is_on
