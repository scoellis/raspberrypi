#!/usr/bin/python
import time
import eeml 
import subprocess # we scrape apcaccess output
interesting = ('bposition') 
res = subprocess.check_output("http://mobile.theride.org/#/dashboard/5")
res_clean = 
for line in res.split('\n'):
    (key,spl,val) = line.partition(': ')
    key = key.rstrip().lower()
    if key in interesting: # just save what we want
        val = val.strip()
        val = val.split(' ',1)[0] # ignore anything after 1st space
        API_KEY = '5hNkK3ChNVUIaTUvmpCnCkaIYDwPndzj02MkF1i4er44Xb2e' # set up pachube connection
        FEED = 777885590
        API_URL = '/v2/feeds/{feednum}.xml' .format(feednum = FEED)
        pac = eeml.Pachube(API_URL, API_KEY) # open up your feed
        pac.update([eeml.Data("APC", val)]) #compile data
        pac.put() # send data to cosm
