from flask import Flask, render_template
import algorithm as al


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def tally():
	location = request.form['location']
	hr = 23
	location_range = al.get_coord_range(location)
	crime_map = al.get_crime_map(location_range, hr)
	danger = al.get_score(location_range, 23)
	violent_map = al.get_violent(crime_map)

	return (danger, violent_map)

