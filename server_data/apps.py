from django.apps import AppConfig


class server_dataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server_data'

    def ready(self):
        from server_data.models import Server
        from server_data import signals
