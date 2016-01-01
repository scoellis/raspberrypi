#!/usr/bin/env python
import time
import serial
import eeml
#import requests
#import json
ser = serial.Serial('/dev/ttyAMA0', 9600)
ser.write('0')
tmp = ser.readline()
print tmp
API_KEY = '5hNkK3ChNVUIaTUvmpCnCkaIYDwPndzj02MkF1i4er44Xb2e'
FEED = 777885590
API_URL = '/v2/feeds/{feednum}.xml' .format(feednum = FEED)
#pac = eeml.cosm(API_URL, API_KEY) # open up your feed
pac = eeml.Pachube(API_URL, API_KEY) # open up your feed
pac.update([eeml.Data("Temperature", tmp, unit=eeml.Fahrenheit())]) #compile data
pac.put() # send data to cosm
#s = requests.session()
#login_header = {'content-type': 'application/json'}
#login_payload = {'username':'Scott Ellis', 'password': 'q!5wrKJH2gbM'}
#r_login = s.post('http://ske313.us/rest/user/login', data=json.dumps(login_payload), headers=login_header)
#token_header = {'content-type': 'application/json'}
#r_token = s.get('http://ske313.us/services/session/token', headers=token_header)
#header = {'content-type': 'application/json', 'X-CSRF-Token': r_token.text}
#payload = {'type':'post_data', 'title':'Temp', 'field_temp':{'und':[{'value':tmp}]}}
#json_data = json.dumps(payload)
#r_node_post = s.post('http://ske313.us/rest/node', data=json_data, headers=header)
#r_logout = s.post('http://ske313.us/rest/user/logout', headers=header)
#file = open("tmp-post.log","a")
#current_time = time.strftime("%m.%d.%y %H:%M",time.localtime())
#file.write("date:" + current_time + " - " + "post status:" + str(r_node_post.status_code) + " - " + "tmp:" + tmp)
