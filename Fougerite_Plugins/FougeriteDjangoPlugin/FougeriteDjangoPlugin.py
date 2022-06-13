__title__ = 'FougeriteDjangoPlugin'
__author__ = 'MrDan4es'
__version__ = '0.0.1'

from datetime import datetime
import json
import clr
clr.AddReferenceByPartialName("Fougerite")
clr.AddReferenceByPartialName('System.Core')
import System
from System import Action
import Fougerite


animals = {'Wolf':':wolf:', 'MutantWolf':':wolf:', 'Bear':':bear:', 'MutantBear':':bear:'}

class FougeriteDjangoPlugin:

    discord_url = 'https://discord.com/api/webhooks/9713459200357*****/*************'
    server_API_url = 'http://127.0.0.1:8000/'

    def webCallback(self, response_code, response):
        Fougerite.Logger.Log(response)

    def loginCallback(self, response_code, response):
        Fougerite.Logger.Log('!!!!!!!' + str(response_code))

    def send_data_API(self, url, method, content):
        Web.CreateAsyncHTTPRequest(
            self.server_API_url + url,
            Action[int, str](self.webCallback),
            method=method,
            inputBody=json.dumps(content),
            contentType="application/json",
        )

    def player_connected_API(self, player):
        Web.CreateAsyncHTTPRequest(
            self.server_API_url + '/api/players/',
            Action[int, str](self.webCallback),
            method='POST',
            inputBody=json.dumps(
                {
                    "steam_ID": player.SteamID,
                    "nickname": player.Name,
                    "on_server": True
                }
            ),
            contentType="application/json",
        )
        Web.CreateAsyncHTTPRequest(
            self.server_API_url + '/api/players/' + player.SteamID + '/',
            Action[int, str](self.webCallback),
            method='PUT',
            inputBody=json.dumps(
                {
                    "steam_ID": player.SteamID,
                    "nickname": player.Name,
                    "on_server": True
                }
            ),
            contentType="application/json",
        )
        # Web.CreateAsyncHTTPRequest(
        #     self.server_API_url + '/api/players/' + player.SteamID + '/',
        #     Action[int, str](self.loginCallback),
        #     method='GET'
        # )

    def discord_post(self, content):
        pass
        # Web.CreateAsyncHTTPRequest(
        #     self.discord_url,
        #     Action[int, str](self.webCallback),
        #     method="POST",
        #     inputBody=json.dumps(content),
        #     contentType="application/json",
        # )

    def On_PlayerConnected(self, Player):
        self.player_connected_API(Player)
        # self.send_data_API(
        #     '/api/players/',
        #     'POST',
        #     {
        #         "steam_ID": Player.SteamID,
        #         "nickname": Player.Name,
        #         "on_server": True
        #     }   
        # )
        # self.send_data_API(
        #     '/api/players/' + Player.SteamID + '/',
        #     'PUT',
        #     {
        #         "steam_ID": Player.SteamID,
        #         "nickname": Player.Name,
        #         "on_server": True
        #     }   
        # )
        self.discord_post(
            {
                'content': '> :bust_in_silhouette: ' + Player.Name + ' connected :green_circle:'
            }
        )

    def On_PlayerDisconnected(self, Player):
        self.send_data_API(
            '/api/players/' + Player.SteamID + '/',
            'PUT',
            {
                "steam_ID": Player.SteamID,
                "nickname": Player.Name,
                "on_server": False
            }   
        )
        self.discord_post(
            {
                'content': '> :bust_in_silhouette: ' + Player.Name + ' disconnected :red_circle:'
            }
        )

    def On_ServerInit(self):
        self.send_data_API(
            '/api/server/1/',
            'PUT',
            {
                'is_on': True
            }
        )
        self.discord_post(
            {
                'content': '> :gear: server is on :green_circle:'
            }
        )

    def On_ServerShutdown(self):
        self.send_data_API(
            '/api/server/1/',
            {
                'is_on': False
            }
        )
        self.discord_post(
            {
                'content': '> :gear: server is off :red_circle:'
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
        Fougerite.Logger.Log('attacker: %s, victim: %s, weapon: %s, damageType: %s, bodyPart: %s' % (attacker, victim, weapon, DeathEvent.DamageType, DeathEvent.DamageEvent.bodyPart))

        if str(DeathEvent.DamageEvent.bodyPart) == 'Head':
            bodyPart = ':exploding_head:'
        else:
            bodyPart = ''

        if attacker != victim:
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
                
            victim = '~~`%s`~~' % (victim)
            self.discord_post(
                {
                    'content': '> :skull_crossbones: : %s %s %s %s' % (attacker, bodyPart, weapon, victim)
                }
            )

        # if attacker == victim:
        #     self.discord_post(
        #         {
        #             'content':':skull_crossbones: ' + victim + ' committed suicide'
        #         }
        #     )
