import requests
import json
import re


class Login():
    def __init__(self):
        pass

    #is important to get session token
    def __new__(self, email, password):
        self.endpoint = "https://serienstream.sx/api/v1/"
        self.token = "9bmkkkvloi4o10pnel886l1xj6ztycualnmofbkrsfzsmc26lrujoesptp8aqw" #Token is from the s.to Android App
        self.email = email
        self.password = password
        data = {
            "email": self.email,
            "password": self.password 
        }
        response = requests.post(f"https://s.to/api/v1/account/login?key={self.token}", data=data).json()
        try:
            self.SSTOSESSION = response['session']
        except:
            return False
        if len(self.SSTOSESSION) < 2:
            return False
        else:
            return {"json": response, "session": self.SSTOSESSION}
class s():

    def __init__(self):
        self.endpoint = "https://serienstream.sx/api/v1/"
        self.token = "9bmkkkvloi4o10pnel886l1xj6ztycualnmofbkrsfzsmc26lrujoesptp8aqw" #Token is from the s.to Android App

    #decompile the series url to id
    def UrlToID(self, url):
        response = requests.get(url).text
        regex = re.compile("series-id=\"(\\d+)\"")
        id = regex.findall(response)[0]
        return id

    #WIP Search
    def Search(self, search):
        search = search.lower().replace(" ", "-")
        return s.UrlToID(self, f"https://serienstream.sx/serie/stream/{search}")

    #option = 0 = all
    #option = 1 = popular
    #option = 2 = new
    #option = 3 = top
    #option = 4 = last seen
    def ListSeries(self, option):
        response = requests.get(f"{self.endpoint}series/list?extended=1&category={option}&key={self.token}")
        return json.loads(response.text)

    #season = 0 = SeriesInfo
    #season = 1 = EpisodeInfosAndListAll
    def GetSeriesInfo(self, id, season):
        response = requests.get(f"{self.endpoint}series/get?series={id}&season={season}&key={self.token}")

        return json.loads(response.text)

    #get Stats from the Stats Page
    def Stats(self):
        response = requests.get(f"{self.endpoint}statistics/get?key={self.token}")
        return json.loads(response.text)


class Watchlist():
    #require session token
    def __init__(self, session):
            print("Attention: You get the token from Login")
            self.token = "9bmkkkvloi4o10pnel886l1xj6ztycualnmofbkrsfzsmc26lrujoesptp8aqw" #Token is from the s.to Android App
            self.SSTOSESSION = session
            self.endpoint = "https://serienstream.sx/api/v1/"

    #list whole watchlist
    def List(self, extended):
            data = {
                "SSTOSESSION": self.SSTOSESSION
            }

            response = requests.get(f"{self.endpoint}account/watchlist/list?key={self.token}&extended={extended}", cookies=data)
            return json.loads(response.text)

    #add a serie to watchlist
    def Add(self, id):
            data = {
                "SSTOSESSION": self.SSTOSESSION
            }

            response = requests.get(f"{self.endpoint}account/watchlist/add?key={self.token}&id={id}", cookies=data)
            return json.loads(response.text)

    #remove a serie from watchlist
    def Remove(self, id):
            data = {
                "SSTOSESSION": self.SSTOSESSION
            }

            response = requests.get(f"{self.endpoint}account/watchlist/remove?key={self.token}&id={id}", cookies=data)
            return json.loads(response.text)

class Subscription():
    #require session token
    def __init__(self, session):
            print("Attention: You get the token from Login")
            self.token = "9bmkkkvloi4o10pnel886l1xj6ztycualnmofbkrsfzsmc26lrujoesptp8aqw" #Token is from the s.to Android App
            self.SSTOSESSION = session
            self.endpoint = "https://serienstream.sx/api/v1/"

    #list whole subscriptions
    def List(self, extended):
        data = {
            "SSTOSESSION": self.SSTOSESSION
        }

        response = requests.get(f"{self.endpoint}account/subscription/list?key={self.token}&extended={extended}", cookies=data)
        return json.loads(response.text)

    #add a serie to subscription
    def Add(self, id):
        data = {
                "SSTOSESSION": self.SSTOSESSION
        }

        response = requests.get(f"{self.endpoint}account/subscription/add?key={self.token}&id={id}", cookies=data)
        return json.loads(response.text)

    #remove a serie from subscription
    def Remove(self, id):
        data = {
            "SSTOSESSION": self.SSTOSESSION
        }

        response = requests.get(f"{self.endpoint}account/subscription/remove?key={self.token}&id={id}", cookies=data)
        return json.loads(response.text)
