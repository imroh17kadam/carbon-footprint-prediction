from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from carbonfootprint.pipeline.prediction import PredictionPipeline



app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            make = object(request.form['make'])
            model = object(request.form['model'])
            vehicle = object(request.form['vehicle'])
            engine_size = float(request.form['engine_size'])
            cylinders = int(request.form['cylinders'])
            transmission = object(request.form['transmission'])
            fuel_type = object(request.form['fuel_type'])
            fuel_consumption_city = float(request.form['fuel_consumption_city'])
            fuel_consumption_hwy = float(request.form['fuel_consumption_hwy'])
            fuel_consumption_comb_km= float(request.form['fuel_consumption_comb_km'])
            fuel_consumption_comb_mpg = float(request.form['fuel_consumption_comb_mpg'])
       
         
            data = [make,model,vehicle,engine_size,cylinders,transmission,fuel_type,fuel_consumption_city,fuel_consumption_hwy,fuel_consumption_comb_km,fuel_consumption_comb_mpg]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080, debug=True)
	# app.run(host="0.0.0.0", port = 8080)