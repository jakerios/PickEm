from curses import use_default_colors
from dataclasses import dataclass
import json
import requests
from requests import Session
from pprint import pprint as pp
import string


class sportsOdds:

    def __init__(self):
        self.apiurl = 'https://api.the-odds-api.com'
        self.session = Session()

    def getSports(self):
        url = self.apiurl + '/v4/sports/?apiKey=3b782c72d90fb790ae55facde42dd3ec'
        r = self.session.get(url)
        print(r.status_code)
        print(r.json())

    def getFootballOdds(self):
        url = self.apiurl + '/v4/sports/americanfootball_nfl/odds/'
        params = {
            'api_key': '3b782c72d90fb790ae55facde42dd3ec',
            'regions': 'us',
            'markets': 'spreads',
            'oddsFormat': 'american',
            'bookmakers': 'draftkings'
        }
        r = requests.get(url, params)
        data = r.json()
        print(data)

        arrFavTeam = []
        arrUndTeam = []
        arrPointSpread = []

        for i in range(len(data)):
            if data[i]['bookmakers'][0]['markets'][0]['outcomes'][0]['point'] <= 0:
                arrFavTeam.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][0]['name'])
                arrUndTeam.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][1]['name'])
                arrPointSpread.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][1]['point'])
            else:
                arrUndTeam.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][0]['name'])
                arrFavTeam.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][1]['name'])
                arrPointSpread.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][0]['point'])

        arrCombinedTeams = arrFavTeam + arrUndTeam

        return arrFavTeam, arrUndTeam, arrPointSpread, arrCombinedTeams
    
    def getHockeyOdds(self):
        url = self.apiurl + '/v4/sports/icehockey_nhl/odds/'
        params = {
            'api_key': '3b782c72d90fb790ae55facde42dd3ec',
            'regions': 'us',
            'markets': 'spreads',
            'oddsFormat': 'american',
            'bookmakers': 'draftkings'
        }
        r = requests.get(url, params)
        data = r.json()
        print(data)

        arrFavTeam = []
        arrUndTeam = []
        arrPointSpread = []

        for i in range(len(data)):
            if data[i]['bookmakers'][0]['markets'][0]['outcomes'][0]['point'] <= 0:
                arrFavTeam.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][0]['name'])
                arrUndTeam.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][1]['name'])
                arrPointSpread.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][1]['point'])
            else:
                arrUndTeam.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][0]['name'])
                arrFavTeam.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][1]['name'])
                arrPointSpread.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][0]['point'])

        arrCombinedTeams = arrFavTeam + arrUndTeam

        return arrFavTeam, arrUndTeam, arrPointSpread, arrCombinedTeams

    def getBaseballOdds(self):
            url = self.apiurl + '/v4/sports/baseball_mlb/odds/'
            params = {
                'api_key': '3b782c72d90fb790ae55facde42dd3ec',
                'regions': 'us',
                'markets': 'spreads',
                'oddsFormat': 'american',
                'bookmakers': 'draftkings'
            }
            r = requests.get(url, params)
            data = r.json()
            print(data)

            arrFavTeam = []
            arrUndTeam = []
            arrPointSpread = []

            for i in range(len(data)):
                if data[i]['bookmakers'][0]['markets'][0]['outcomes'][0]['point'] <= 0:
                    arrFavTeam.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][0]['name'])
                    arrUndTeam.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][1]['name'])
                    arrPointSpread.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][1]['point'])
                else:
                    arrUndTeam.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][0]['name'])
                    arrFavTeam.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][1]['name'])
                    arrPointSpread.append(data[i]['bookmakers'][0]['markets'][0]['outcomes'][0]['point'])

            arrCombinedTeams = arrFavTeam + arrUndTeam

            return arrFavTeam, arrUndTeam, arrPointSpread, arrCombinedTeams
