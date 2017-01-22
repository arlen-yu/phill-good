from flask import Flask, render_template, request
import algorithm as al
import parse_sqlite as ps


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def tally():
	location = request.form['address']

	#keyPoint: [name, lat, lng, description HTML]

	# crime info
	hr = 23
	location_range = al.get_coord_range(location)
	crime_map = al.get_crime_map(location_range, hr)
	danger = al.danger_decile(al.get_score(location_range, 23))
	violent_map = al.get_violent(crime_map)


	# police info
	coords = al.get_coords(location)
	police_result = ps.get_closest_location(coords[0], coords[1], "police_stations")
	closest_police = police_result[0][4]
	telephone = police_result[0][5]
	police_html = "<strong>Nearest Police Station</strong><br>Address: " + closest_police + "<br> Phone: " + str(telephone)
	police_kp = [closest_police, police_result[1], police_result[2], police_html]

	#correctional info
	correctional_result = ps.get_closest_location(coords[0], coords[1], "correctional")
	closest_correctional = correctional_result[0][3]
	c_telephone = correctional_result[0][8]
	correctional_html = "<strong>Nearest Correctional Facility</strong><br>Address: " + closest_correctional + "<br> Phone: " + str(c_telephone)
	

	#healthy screening info
	health_result = ps.get_closest_location(coords[0], coords[1], "heart_healthy")
	closest_health = health_result[0][5]
	h_telephone = health_result[0][12]
	health_html = "<strong>Nearest Health Screening Facility</strong><br>Address: " + closest_health + "<br> Phone: " +str(h_telephone)

	#farmers market
	farmers_result = ps.get_closest_location(coords[0], coords[1], "farmers_market")
	closest_market = farmers_result[0][5]
	h_description = farmers_result[0][6]
	

	#chinese food
	chinese_result = ps.get_closest_location(coords[0], coords[1], "chinese")
	closest_chinese = chinese_result[0][3]
	chinese_name = chinese_result[0][4]

	#parks and rec
	parks_result = ps.get_closest_location(coords[0], coords[1], "parks")
	closest_parks = parks_result[0][3]
	parks_address = parks_result[0][4]

	#corner stores
	corner_result = ps.get_closest_location(coords[0], coords[1], "corner_stores")
	closest_corner = corner_result[0][3]
	corner_address = corner_result[0][4]

	#health centers
	hcenter_result = ps.get_closest_location(coords[0], coords[1], "health_centers")
	closest_hcenter = hcenter_result[0][9]


	return render_template('index.html', danger=danger,safe=(100-danger), 
		violent_map=violent_map, closest_police=closest_police, closest_correctional=closest_correctional,
		closest_health=closest_health, closest_market=closest_market, h_description=h_description,
		closest_chinese=closest_chinese, chinese_name=chinese_name, closest_parks=closest_parks,
		parks_address=parks_address, closest_corner=closest_corner, corner_address=corner_address,
		closest_hcenter=closest_hcenter)

