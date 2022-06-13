__title__ = 'DjangoAPI'
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


server_API_url = 'http://127.0.0.1:8000/'


class DjangoAPI:
    '''Simple Fougerite plugin with custom server API support'''
    def web_callback(self, response_code, response):
        Fougerite.Logger.Log(response)

    def login_callback(self, response_code, response):
        Fougerite.Logger.Log('!!!!!!!' + str(response_code))

    def send_data_API(self, url, method, content):
        Web.CreateAsyncHTTPRequest(
            self.server_API_url + url,
            Action[int, str](self.web_callback),
            method=method,
            inputBody=json.dumps(content),
            contentType="application/json",
        )

    def player_connected_API(self, player):
        Web.CreateAsyncHTTPRequest(
            self.server_API_url + '/api/players/',
            Action[int, str](self.web_callback),
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
            Action[int, str](self.web_callback),
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
        #     Action[int, str](self.login_callback),
        #     method='GET'
        # )

    def On_PlayerConnected(self, Player):
        self.player_connected_API(Player)

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

    def On_ServerInit(self):
        self.send_data_API(
            '/api/server/1/',
            'PUT',
            {
                'is_on': True
            }
        )

    def On_ServerShutdown(self):
        self.send_data_API(
            '/api/server/1/',
            'PUT',
            {
                'is_on': False
            }
        )

    def On_Chat(self, Player, ChatEvent):
        pass
