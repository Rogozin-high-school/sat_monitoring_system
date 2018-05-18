import urllib.parse
import urllib.request
import urllib.response
import urllib
import json
class Communication:
    def __init__(self, url):
        self.url = url
        self.res = []
    def send(self, msg):
        print (json.dumps(msg.dict))
        data = bytes(json.dumps(msg.dict), "utf-8")
        res = urllib.request.urlopen(self.url + "/set.php", data)
        #data = response.read().decode("utf-8")
    def get_var(self, name):
        data = bytes(json.dumps([{"id" : name}]), "utf-8")
        res = urllib.request.urlopen(self.url + "/get.php", data)
        return res.read()
    def recv():
        return self.res.pop()

class OutMsg:
    def __init__(self):
        self.dict = {}
    def add_var(self, name, value):
        self.dict[name] = value

