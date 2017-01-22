import sqlite3

conn = sqlite3.connect('crimes.db')
c = conn.cursor()

#arbitrary crime score table
crimeRating = {'Aggravated Assault Firearm':8, 'Aggravated Assault No Firearm':5, 'All Other Offenses':2, 
'Arson':8, 'Burglary Residential': 5, 'Burglary Non-Residential':3, 'Disorderly Conduct':3, 'DRIVING UNDER THE INFLUENCE':2,
'Embezzlement':1, 'Forgery and Counterfeiting':1, 'Fraud': 1, 'Homicide - Criminal': 18, 'Liquor Law Violations':1,
'Motor Vehicle Theft':5, 'Narcotic / Drug Law Violations': 5, 'Other Assaults': 7, 'Other Sex Offenses (Not Commercialized)':6,
'Prostitution and Commercialized Vice':3, 'Public Drunkenness':2, 'Rape':10, 'Robbery Firearm':8, 'Robbery No Firearm':5,
'Theft from Vehicle':5, 'Thefts':4, 'Vagrancy/Loitering':2, 'Gambling Violations':0, 'Offenses Against Family and Children':0, 'Receiving Stolen Property':0, 'Recovered Stolen Motor Vehicle':0, 'Vandalism/Criminal Mischief':3, 'Weapon Violations':3}

# returns a hashmap of the number of each crime, and total "crime score"
def crime_map(locations, hr):
	crime_map = {'Score':0}

	maxhr = (hr - 22) if (hr + 2 > 23) else (hr + 2)
	minhr = (hr + 22) if (hr - 2 < 0) else (hr - 2)
	if (hr >= 22 or hr <= 2):
		result = c.execute("SELECT crime FROM data WHERE (x >= ? AND  x <= ?) AND (y >= ? AND y <= ?) AND (hour >= ? OR hour <= ?)", 
		(locations[0], locations[1], locations[2], locations[3], minhr, maxhr))
	else:
		result = c.execute("SELECT crime FROM data WHERE (x >= ? AND  x <= ?) AND (y >= ? AND y <= ?) AND (hour >= ? AND hour <= ?)", 
		(locations[0], locations[1], locations[2], locations[3], minhr, maxhr))

	for i in result:
		crime_map['Score'] = crime_map['Score'] + crimeRating[str(i[0])]
		if i[0] in crime_map:
			crime_map[i[0]] = crime_map[i[0]] + 1
		else:
			crime_map[i[0]] = 1

	return crime_map



