#!/usr/bin/env python3

import requests

path = 'packet.oldest.filetime'
payload = {'msg': 'get', 'force-content-type': 'application/json'}
url = 'http://netwitness:50104/database/stats/packet.oldest.file.time'

resp = requests.get(url, auth=('admin', 'netwitness'), params=payload)
print (resp.json())