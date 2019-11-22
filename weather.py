from flask import Flask, render_template, request 
import json 
import urllib.request 


# Flask constructor takes the name of  
# current module (__name__) as argument. 
app = Flask(__name__) 

@app.route('/', methods =['POST', 'GET']) 
def weather(): 
	if request.method == 'POST': 
		city = request.form['city'] 
	else: 
		# for default name mumbai 
		city = 'mumbai'

	# API key 
	# api = 'ae4b99fcae74c6481413e410d182e520'

	# source contain json data from api 
	source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q =' + city + '&appid =' + api).read() 

	# converting JSON data to a dictionary 
	list_of_data = json.loads(source) 

	# data for variable list_of_data 
	data = { 
		"country_code": str(list_of_data['sys']['country']), 
		"coordinate": str(list_of_data['coord']['lon']) + ' '
					+ str(list_of_data['coord']['lat']), 
		"temp": str(list_of_data['main']['temp']) + 'k', 
		"pressure": str(list_of_data['main']['pressure']), 
		"humidity": str(list_of_data['main']['humidity']), 
	} 
	print(data) 
	return render_template('index.html', data = data) 



if __name__ == '__main__': 
	app.run(debug = True) 
