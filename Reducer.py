#!/usr/bin/env python
'''
@author: 
'''

import sys
import time
import re 
from geoip import geolite2

def convert_time(d, utc):
#    d = "14/Jan/2014:09:36:50"
#    utc = '-0800' 

    fmt ='%d/%b/%Y:%H:%M:%S'
    utci = int(utc)
    
    epot = time.mktime(time.strptime(d, fmt))    
    epod = (abs(utci) % 100)/60.0 + (abs(utci) // 100)
       
    if utc.isdigit():
        epf = epot + epod*3600
    else:
        epf = epot - epod*3600

    return int(epf)  

#Iterate through every line passed in to stdin
print ("Epoch Time\t IP Address\t (Latitude, Longitude)\t URI\t\t\t Referer")
for input in sys.stdin.readlines():
    logline = input.strip()
    
    _logregex = re.compile(r'^(\S+) (\S+) (\S+) \[([^:]+:\d+:\d+:\d+) ([^\]]+)\] \"(\S+) \/(.*?) (\S+)\" (\S+) (\S+) "([^"]*)" "([^"]*)"$')    
    
    #process log files by way of parsing 
    m = re.match(_logregex, logline)


    
    if m:
	pline = []
        try:
            ipmatch = geolite2.lookup(m.group(1))
        except:
            ipmatch = None
            
        if ipmatch is not None:
#                    print m.group(4)
            pline.append(convert_time(m.group(4), m.group(5)))
            pline.append(m.group(1))
            pline.append(ipmatch.location)
            pline.append(m.group(7))
            pline.append(m.group(11))
            #                    pline.append(ipmatch.country)

        else:
            pline.append(convert_time(m.group(4), m.group(5)))
            pline.append(m.group(1))
            pline.append('N/A')
            pline.append(m.group(7))
            pline.append(m.group(11))                    

    	print (''.join([ (str(x) + '\t')  for x in pline])) # Convert list into string
#    	print (''.join(map(str,pline))) # Convert list into string
    
    
