from django.shortcuts import  render

from server_data.models import ChatMessage, Player, Server


def index_page(request): 
    server = Server.objects.get(pk=1)
    messages = ChatMessage.objects.all()
    online_players = None
    if server.is_on:
        online_players = Player.objects.filter(on_server=True)

    return render(
        request,
        'index.html', 
        {
            'server':server,
            'messages': messages,
            'players': online_players
        }
    )
