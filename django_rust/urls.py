from django.urls import include, path
from django.contrib import admin

from rest_framework.routers import SimpleRouter

from server_data.views import PlayerViewSet, ServerViewSet
from .views import index_page


router = SimpleRouter()
router.register(r'server', ServerViewSet, basename='server')
router.register(r'players', PlayerViewSet, basename='players')

urlpatterns = [
    path('', index_page, name='index'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
