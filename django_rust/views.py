from django.shortcuts import  render

from server_data.models import Server


def index_page(request): 
    server = Server.objects.get(pk=1)

    return render(
        request,
        'index.html', 
        {
            'server':server
        }
    )
