from django.contrib import admin

from server_data.models import ChatMessage, Player, Server


@admin.register(Server)
class CharListAdmin(admin.ModelAdmin):
    list_display = ('is_on', 'pk')
    

@admin.register(Player)
class CharListAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'on_server')


@admin.register(ChatMessage)
class CharListAdmin(admin.ModelAdmin):
    list_display = ('get_nickname', 'create_date')

    def get_nickname(self, obj):
        return obj.player.nickname
