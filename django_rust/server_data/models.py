from django.db import models


class Player(models.Model):
    steam_ID = models.PositiveIntegerField(unique=True)
    nickname = models.CharField(max_length=30)
    on_server = models.BooleanField(default=False)


class Server(models.Model):
    is_on = models.BooleanField(default=False)
