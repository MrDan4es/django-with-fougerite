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
                'command': 'server',
                'online': is_online
            }
        )

    async def websocket_server(self, event):
        await self.send_json(
            {
                'command': event['command'],
                'online': event['online']
            }
        )

    async def websocket_player(self, event):
        await self.send_json(
            {
                'command': event['command'],
                'nickname': event['nickname'],
                'on_server': event['on_server']
            }
        )
        
    async def websocket_chat(self, event):
        await self.send_json(
            {
                'command': event['command'],
                'nickname': event['nickname'],
                'create_date': event['create_date'],
                'text': event['text']
            }
        )

    @database_sync_to_async
    def is_server_online(self) -> bool:
        return Server.objects.get(pk=1).is_on
