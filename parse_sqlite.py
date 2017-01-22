import sqlite3

conn = sqlite3.connect('crimes.db')
c = conn.cursor()


#simple distance between two lng/lat pairs
def distance(l1, l2):
	d = ((l1[0] - l2[0])**2 + (l1[1] - l2[1])**2)**0.5
	return d


#gets the closest location from a certain longitude and latitude
def get_closest_location(lng, lat, tablename): #table_ref is the column num on the desired info
	result = c.execute("SELECT * FROM %s" % tablename)

	min_location = [100, 100, 100, 100] #row, lat, long, dist

	for el in result:
		d = distance((lng, lat), (el[0], el[1]))
		if d <= min_location[3]:
			min_location[0] = el
			min_location[1] = lat
			min_location[2] = lng
			min_location[3] = d

	return min_location




