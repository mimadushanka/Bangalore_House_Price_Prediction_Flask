from flask import Flask, render_template,request,jsonify
from . import util
import os
# Tell Flask where to look for templates
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response=jsonify({
        'locations':util.get_location_names()
   } )
    response.headers.add('Access-control-Allow-Origin','*')
    return response


@app.route('/', methods=['GET', 'POST'])
def home():
    locations = util.get_location_names() or []
   # print("LOCATIONS:", locations)
    if request.method == 'POST':
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = request.form['bhk']
        bath = request.form['bath']

        estimated_price = util.get_estimated_price(location, float(total_sqft),int(bhk),int(bath))
        return render_template('client/app.html',
                               locations=locations,
                               estimated_price=estimated_price,
                               selected_sqft=total_sqft,
                               selected_bhk=bhk,
                               selected_bath=bath,
                               selected_location=location)
 
    return render_template('client/app.html', locations=locations)

if __name__=="__main__":
    print("starting the flask server")
    util.load_saved_artifacts()
    app.run()