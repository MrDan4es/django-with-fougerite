from django.db import models
from django.utils import timezone


class Player(models.Model):
    steam_ID = models.PositiveIntegerField(unique=True)
    nickname = models.CharField(max_length=30)
    on_server = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname


class ChatMessage(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)


class Server(models.Model):
    is_on = models.BooleanField(default=False)
