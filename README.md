#Apache Web Log Parsing with Map Reduce


This Map Reduce code reads the given apache Web log with the following schema:  
198.0.200.105 - - [14/Jan/2014:09:36:50 -0800] "GET /svds.com HTTP/1.1" 301 241 "http://www.svds.com/rockandroll/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"
- Remote host (ie the client IP)
- Identity of the user determined by identd (not usually used since not reliable)
- User name determined by HTTP authentication
- Time the server finished processing the request.
- Request line from the client. ("GET / HTTP/1.0")
- Status code sent from the server to the client (200, 404 etc.)
- Size of the response to the client (in bytes)
- Referer is the page that linked to this URL.
- User-agent is the browser identification string.

The code then uses the extracted IP address to lookup latitude and longtitude utilizing [GEOIP] (http://www.maxmind.com) database. It then 
use the extracted date and time and convert it into Epoch format and then writes the following to the output file:
- Epoch Time (date and time the request was processed by the server)
- IP Address 
- Latitude, Longitude
- URI (user click on from the data file)
- Referer (from the data file)

