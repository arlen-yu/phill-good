import csv, time

empty = []

#myfile = csv.writer(open( "revised_crime.csv", 'w'))

f = csv.reader(open('crime_data.csv'))

counter = 0

for row in f:
	if (counter == 0):
		row[len(row[0])-2] = ["potato","egg"]
		counter+=1
	else:
		break

for row in f:
	if (row[len(row)-2] != ''):
	 	 new_row = row[len(row)-2].split(" ")
	 	 row[len(row)-2] = new_row[1]+", "+new_row[2]
	 	 empty.append(row)
	 	 print row
	 	 #ime.sleep(2)

print empty, len(empty)