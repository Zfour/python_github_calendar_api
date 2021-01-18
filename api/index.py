# -*- coding: UTF-8 -*-
import requests
import re
from http.server import BaseHTTPRequestHandler
import json

gitpage = requests.get("https://github.com/Zfour")
data = gitpage.text

contributionsreg = re.compile('<h2 class="f4 text-normal mb-2">(.*?)contributions')
datadatereg = re.compile(r'data-date="(.*?)"/>')
datacountreg = re.compile(r'data-count="(.*?)" data-date')

datadate = datadatereg.findall(data)
datacount = datacountreg.findall(data)
datacount =list(map(int, datacount))
contributions = sum(datacount)

datalist=[]
for index,item in enumerate(datadate):
    itemlist = {"date":item,"count":datacount[index]}
    datalist.append(itemlist)

returndata = {
    "tatal":contributions,
    "contributions":[
        datalist
  ]

}

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps(returndata).encode('utf-8'))
        return
