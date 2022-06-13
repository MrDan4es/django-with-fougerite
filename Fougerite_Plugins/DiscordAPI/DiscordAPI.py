__title__ = 'DiscordAPI'
__author__ = 'MrDan4es'
__version__ = '0.0.1'


import clr
clr.AddReferenceByPartialName("Fougerite")
clr.AddReferenceByPartialName('System.Core')

from datetime import datetime
import json
import System
from System import Action
import Fougerite


discord_url = 'https://discord.com/api/webhooks/9713459200357*****/LpfCPPxMmf102Z5jMoJaX3XWM-qjFR1FfKoupOddbfCI5RY6URNWLEmnz4Bq4xn*****'
animals = {'Wolf':':wolf:', 'MutantWolf':':wolf:', 'Bear':':bear:', 'MutantBear':':bear:'}


class DiscordAPI:
    '''Simple Fougerite plugin with Discord API support'''
    def web_callback(self, response_code, response):
        Fougerite.Logger.Log(str(response_code))

    def discord_post(self, content):
        Web.CreateAsyncHTTPRequest(
            discord_url,
            Action[int, str](self.web_callback),
            method="POST",
            inputBody=json.dumps(content),
            contentType="application/json",
        )

    def On_ServerInit(self):
        self.discord_post(
            {
                'content': '> :gear: server is on :green_circle:'
            }
        )

    def On_ServerShutdown(self):
        self.discord_post(
            {
                'content': '> :gear: server is off :red_circle:'
            }
        )

    def On_PlayerConnected(self, Player):
        self.discord_post(
            {
                'content': '> :bust_in_silhouette: ' + Player.Name + ' connected :green_circle:'
            }
        )

    def On_PlayerDisconnected(self, Player):
        self.discord_post(
            {
                'content': '> :bust_in_silhouette: ' + Player.Name + ' disconnected :red_circle:'
            }
        )

    def On_Chat(self, Player, ChatEvent):
        self.discord_post(
            {
                "embeds": [
                    {
                        "description": ChatEvent.OriginalMessage[1:-1],
                        "timestamp": datetime.utcnow().isoformat(),
                        "author": {
                            "name": Player.Name,
                        },
                    }
                ]
            }
        )

    def On_PlayerKilled(self, DeathEvent):
        attacker = DeathEvent.Attacker.Name
        victim = DeathEvent.Victim.Name
        weapon = DeathEvent.WeaponName
        bodyPart = ''

        if attacker == victim:
            return

        victim = '~~`%s`~~' % (victim)

        if str(DeathEvent.DamageEvent.bodyPart) == 'Head':
            bodyPart = ':exploding_head:'

        if attacker in animals.keys():
            attacker = animals[attacker]
            weapon = ':feet:'
        elif weapon in ['Large Spike Wall', 'Spike Wall']:
            attacker = '`%s`' % (DeathEvent.Attacker.Creator.Name)
            weapon = ':drop_of_blood:(***%s***)' % (weapon)
        else:
            if weapon in ['F1 Grenade', 'Explosive Charge']:
                weapon = ':boom:(***%s***)' % (weapon)
            elif weapon in ['P250', '9mm Pistol', 'Revolver', 'HandCannon']:
                weapon = ':gun:(***%s***)' % (weapon)
            elif weapon in ['Hatchet', 'Pick Axe', 'Rock', 'Stone Hatchet']: 
                weapon = ':dagger:(***%s***)' % (weapon)
            elif weapon == 'Hunting Bow':
                weapon = ':bow_and_arrow:(***%s***)' % (weapon)
            else:
                weapon = ':crossed_swords:(***%s***)' % (weapon)
            attacker = '`%s`' % (attacker)
            
        self.discord_post(
            {
                'content': '> :skull_crossbones: : %s %s %s %s' % (attacker, bodyPart, weapon, victim)
            }
        )
