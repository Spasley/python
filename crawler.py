__author__ = 'Volodka'

import requests
import base64
from basicauth import encode

base_url = "https://dev.trialpay.com:4850"
login = 'kolenov'
password = 'nsnshrb%%765'

s = requests.Session()

#s.auth = ('kolenov', 'nsnshrb%%765')
#data = {"login": "kolenov", "pass": "nsnshrb%%765"}

s = requests.post((base_url+params))

'''headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': ('Basic ' + creds),
           'Content-Length': '0'}

#r = s.post(base_url, headers=headers)
#print(headers)
#print(s.cookies)
#print(r.text)'''
