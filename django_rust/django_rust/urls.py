from django.urls import include, path, re_path
from django.contrib import admin

from rest_framework.routers import SimpleRouter

from server_data.views import PlayerViewSet, ServerViewSet
from .views import index_page
from .consumers import MainConsumer


router = SimpleRouter()
router.register(r'server', ServerViewSet, basename='server')
router.register(r'players', PlayerViewSet, basename='players')

urlpatterns = [
    path('', index_page, name='index'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]

websocket_urlpatterns = [
    re_path(r'ws/$', MainConsumer.as_asgi()),
]
