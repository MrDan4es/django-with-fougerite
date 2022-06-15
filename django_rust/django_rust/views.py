from django.shortcuts import  render

from server_data.models import ChatMessage, Server


def index_page(request): 
    server = Server.objects.get(pk=1)
    messages = ChatMessage.objects.all()

    return render(
        request,
        'index.html', 
        {
            'server':server,
            'messages': messages
        }
    )
