#!/usr/bin/env python3

import requests
import sys
import getpass
from datetime import datetime, timedelta

"""
HTTP GET
"""
def httpGet(host, port, path):
	url = "http://%s%s%s%s&force-content-type=text/plain" % (host, ":", port, path)
	r = requests.get(url, auth=(user, passwd))
	calculateDays(host, r.content.strip())

def calculateDays(host, pktDate):
	pktDateConverted = datetime.strptime(pktDate, '%Y-%b-%d %H:%M:%S')
	today = datetime.now()
	todayConverted = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	todayConverted = datetime.strptime(todayConverted, '%Y-%m-%d %H:%M:%S')
	delta = todayConverted - pktDateConverted

	print "Host: %s\tPacket Oldest Time: %s\t\tRaw Retention: %s" % (host, pktDateConverted, delta)

""" 
"main" logic 
"""
user = raw_input("Username:")
passwd = getpass.getpass("Password for " + user + ":")

f = open('devices_decoders.csv', 'r')
for line in f.readlines():
	line = line.strip()
	httpGet(line, "50104", "/database/stats/packet.oldest.file.time?msg=get")
