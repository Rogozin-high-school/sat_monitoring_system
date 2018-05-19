"""
Connection module for a remote data hub
Author: Yotam Salmon
"""

import json
import urllib.request

class DataHub(object):

    def __init__(self, addr):
        if addr.endswith("/"):
            self.addr = addr[:-1]
        else:
            self.addr = addr

        self._get = "/get.php"
        self._set = "/set.php"

    def set_endpoints(self, get, set):
        self._get = get
        self._set = set

    def get(self, vars):
        body = bytes(json.dumps([{"id": x} if type(x) == str else x for x in vars]), "utf-8")
        req = urllib.request.urlopen(self.addr + self._get, body)
        res = req.read()
        return json.loads(str(res, "utf-8"))

    def set(self, vals):
        body = bytes(json.dumps([{"id": x, "value": y} for x, y in vals.items()]), "utf-8")
        req = urllib.request.urlopen(self.addr + self._set, body)
        res = req.read()
        return json.loads(str(res, "utf-8"))