import urllib.parse
import urllib.request
import urllib
import json
import time
class Connection:
    def __init__(self, url):
        self.url = url
        self.res = []
    def send(self, msg):
        print (json.dumps(msg.dict))
        data = bytes(json.dumps(msg.dict), "utf-8")
        t = time.time()
        res = urllib.request.urlopen(self.url + "/set.php", data)
        data = res.read().decode("utf-8")
        print(data)
        print("time for response: " + str(time.time() - t))
    
    def get_var(self, name, password = ''):
        data = bytes(json.dumps([{"id" : name, "password" : password}]), "utf-8")
        res = urllib.request.urlopen(self.url + "/get.php", data)
        return json.loads(res.read().decode("utf-8"))
    
    def recv():
        return self.res.pop()

class OutMsg:
    def __init__(self):
        self.dict = []
    def add_var(self, name, value):
        d = {
            "id" : name,
            "value" : value
        }
        self.dict.append(d)

