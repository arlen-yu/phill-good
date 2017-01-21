import json
from urllib2 import urlopen
import requests

limit = 69;
url = "https://data.phila.gov/resource/sspu-uyfa.json?%24limit=10"

# response = urlopen(url)
# print response
# data = json.loads(str(response.read()))
response = requests.get(url)
if response.status_code == 200:
	data = response.json()
	print data
else:
	print "f***"


def swag(location, my_time):
	crimes = {}
	for i in data:
		time_s = data[i]['dispatch_time']
		time = int(time_s.strip(':').lstrip('0'))
		r = 2
		if 'shape' in data[i] and time <= my_time[0] and time >= my_time[1]:
			crimes[data[i]['text_general_code']] = crimes[data[i]['text_general_code']] + 1 #what if doesn't exist?
	return crimes



