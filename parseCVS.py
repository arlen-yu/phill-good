import json
# import requests
import urllib2
from pprint import pprint
import sqlite3

conn = sqlite3.connect('crime.db')
c = conn.cursor()


shit = c.execute('''SELECT * FROM data WHERE shape REGEXP ''')


# pprint(records)

# def swag(location, my_time):
# 	crimes = {}
# 	for i in records:
# 		# time_s = i['DISPATCH_TIME']
# 		# time = int(time_s.strip(':').lstrip('0'))
# 		r = 2
# 		#if 'shape' in data[i]: #and time <= my_time[0] and time >= my_time[1]
# 		crime = i['TEXT_GENERAL_CODE']
# 		if crime in crimes:
# 			crimes[crime] = crimes[crime] + 1
# 		else:
# 			crimes[crime] = 1
# 		#crimes[i['TEXT_GENERAL_CODE']] = crimes[i['TEXT_GENERAL_CODE']] + 1 #what if doesn't exist?
# 	return crimes

# print swag(123, 1400)

