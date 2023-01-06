# -*- coding: UTF-8 -*-
import requests
import re
from http.server import BaseHTTPRequestHandler
import json

def list_split(items, n):
    return [items[i:i + n] for i in range(0, len(items), n)]

def getdata(name):
    gitpage = requests.get("https://github.com/" + name)
    data = re.findall('data-date="(.*?)" data-level="\d+" rx="\d+" ry="\d+">(.*?) contribution',
                      gitpage.text)
    datalist = [{"date": _[0], "count": 0 if _[1] == 'No' else int(_[1])} for _ in data]
    datalistsplit = list_split(datalist, 7)
    returndata = {
        "total": sum([_["count"] for _ in datalist]),
        "contributions": datalistsplit
    }
    return returndata

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        user = path.split('?')[1]
        data = getdata(user)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
