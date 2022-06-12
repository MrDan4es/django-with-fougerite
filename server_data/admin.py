from django.contrib import admin

from server_data.models import Player, Server


@admin.register(Server)
class CharListAdmin(admin.ModelAdmin):
    list_display = ('is_on', 'pk')
    

@admin.register(Player)
class CharListAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'on_server')
