from datetime import datetime
import googlemaps
import json
from pprint import pprint
import parseCVS

k = 'AIzaSyAhTTvizt-cR4hE-7nlEy84ZNISya8VrVo'

#aggravated assault firearm 8
# Aggravated Assault No Firearm 5
# Arson 8
#all other offensive 2
#Burglary Non-Residential 3
#Burglary Residential 5
#disorderly conduct 3
#driving under the influence 2
#Embezzlement 1
#Forgery and Counterfeiting
#fraud 0
#Homicide - Criminal 10
#Liquor Law Violations 1
#motor vehicle theft 5
#narcotic/drug law 5
#other assaults 7
#other sex offensive (non commercial) 6
#prostitution  3
#public drunkenness 2
#rape 10
#recovered stolen motor vehicle 0
#robbery firearm  8
#robbery no firearm 5
#theft from vehicle 5
#theft 4
#vagrancy/loitering 2
#vandalism/mischief 3
#weapon violation 3

crime_levels = {'Aggravated Assault Firearm':8, 'Aggravated Assault No Firearm':5, 'All Other Offenses':2, 
'Arson':8, 'Burglary Residential': 5, 'Burglary Non-Residential':3, 'Disorderly Conduct':3, 'DRIVING UNDER THE INFLUENCE':2,
'Embezzlement':1, 'Forgery and Counterfeiting':1, 'Fraud': 1, 'Homicide - Criminal': 40, 'Liquor Law Violations':1,
'Motor Vehicle Theft':5, 'Narcotic / Drug Law Violations': 5, 'Other Assaults': 7, 'Other Sex Offenses (Not Commercialized)':6,
'Prostitution and Commercialized Vice':3, 'Public Drunkenness':2, 'Rape':20, 'Robbery Firearm':19, 'Robbery No Firearm':10,
'Theft from Vehicle':5, 'Thefts':4, 'Vagrancy/Loitering':2, 'Vandalism/Criminal Mischief':3, 'Weapon Violations':3}

def get_coord_range(location):
	gmaps = googlemaps.Client(key=k)
	geocode_result = gmaps.geocode(location + ', Philadelphia')
	lat = geocode_result[0]['geometry']['location']['lat']
	lng = geocode_result[0]['geometry']['location']['lng']
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


