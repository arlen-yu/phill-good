from datetime import datetime
import googlemaps
import json
from pprint import pprint
import parseCVS

k = 'AIzaSyB5KrR1c9rSfs2uCvtoqzB8OGwr80HNC7M'


crime_levels = {'Aggravated Assault Firearm':8, 'Aggravated Assault No Firearm':5, 'All Other Offenses':2, 
'Arson':8, 'Burglary Residential': 5, 'Burglary Non-Residential':3, 'Disorderly Conduct':3, 'DRIVING UNDER THE INFLUENCE':2,
'Embezzlement':1, 'Forgery and Counterfeiting':1, 'Fraud': 1, 'Homicide - Criminal': 40, 'Liquor Law Violations':1,
'Motor Vehicle Theft':5, 'Narcotic / Drug Law Violations': 5, 'Other Assaults': 7, 'Other Sex Offenses (Not Commercialized)':6,
'Prostitution and Commercialized Vice':3, 'Public Drunkenness':2, 'Rape':20, 'Robbery Firearm':19, 'Robbery No Firearm':10,
'Theft from Vehicle':5, 'Thefts':4, 'Vagrancy/Loitering':2, 'Vandalism/Criminal Mischief':3, 'Weapon Violations':3}


def get_coords(location):
	gmaps = googlemaps.Client(key=k)
	geocode_result = gmaps.geocode(location + ', Philadelphia')
	lat = geocode_result[0]['geometry']['location']['lat']
	lng = geocode_result[0]['geometry']['location']['lng']
	return (lng,lat)

def get_coord_range(location):
	lng, lat = get_coords(location)
	lat_low = lat - 0.005000
	lat_high = lat + 0.005000
	lng_low = lng - 0.005000
	lng_high = lng + 0.005000
	r = [lng_low, lng_high, lat_low, lat_high]
	return r


def time_range(time):
	pass

def get_crime_val(crime, location, time):
	num = len(parseCVS.swag(crime, location, time))
	val = crime_levels.get(crime)
	return num * val

def danger_decile(score):
	if score < 175:
		return 10
	elif score < 435:
		return 20
	elif score < 635:
		return 30
	elif score < 880:
		return 40
	elif score < 1330:
		return 50
	elif score < 2165:
		return 60
	elif score < 2775:
		return 70
	elif score < 3560:
		return 80
	elif score < 4825:
		return 90
	else:
		return 100


def get_violent(crime_map):
	violent_map = {'Score':0, 'Minor':0,'Aggravated Assault Firearm':0, 'Aggravated Assault No Firearm':0, 'Homicide - Criminal':0,
'Motor Vehicle Theft':0, 'Other Assaults':0, 'Other Sex Offenses (Not Commercialized)':0, 'Rape':0, 'Robbery Firearm':0, 'Robbery No Firearm':0,'Weapon Violations':0}
	
	for key in crime_map:
		if key in violent_map:
			violent_map[key] = crime_map[key]
		else:
			violent_map['Minor'] = violent_map['Minor'] + crime_map[key]

	return violent_map

def get_crime_map(location, hr):
	return parseCVS.crime_map(location, hr)

def get_score(location, hr):
	return get_crime_map(location, hr)['Score']

#print get_coords("10 durfor street")
