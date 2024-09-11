import pickle
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler
from flask import Flask, jsonify , render_template

application = Flask(__name__)
app = application

## import ridge regressor and standard scalar pickle
ridge_model = pickle.load(open('models/ridge.pkl' , 'rb'))
standard_scalar = pickle.load(open('models/scaler.pkl' , 'rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata' , methods = ['GET' , 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.grt('RH'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(reqest.form.get('Rain'))
        FFMC = float(reqest.form.get('FFMC'))
        DMC = float(reqest.form.get('DMC'))
        ISI = float(reqest.form.get('ISI'))
        Classes = float(reqest.form.get('Classes'))
        Region = float(reqest.form.get('Region'))


        new_data_scaled = standard_scalar.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(new_data_scaled)

        return render_template('home.html',results = result[0])
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")
