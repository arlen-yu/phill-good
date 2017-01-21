import fileinput
import parseCVS
import algorithm

f = fileinput.input(files='Roads.txt')

def testRoads():
	result = {}
	   
	for line in f:
		loc = algorithm.get_coord_range(line)
		score = parseCVS.crime_map(loc, 20)['Score']
		if score in result:
			result[score] = result[score] + 1
			print score
		else:
			result[score] = 1
			print score

	f.close()

	return result;

print testRoads()