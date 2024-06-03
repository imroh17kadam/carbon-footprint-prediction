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


@app.route('/predict', methods=['POST'])
def index():
    try:
        # Read the inputs given by the user
        Engine_Size = float(request.form['Engine Size(L)'])
        Cylinders = int(request.form['Cylinders'])
        Transmission_A10 = request.form['Transmission_A10']  # Assuming transmission is a string

        Transmission_A10 = 0
        Transmission_A4 = 0
        Transmission_A5 = 0
        Transmission_A6 = 0
        Transmission_A7 = 0
        Transmission_A8 = 0
        Transmission_A9 = 0
        Transmission_AM5 = 0
        Transmission_AM6 = 0
        Transmission_AM7 = 0
        Transmission_AM8 = 0
        Transmission_AM9 = 1
        Transmission_AS10 = 0
        Transmission_AS4 = 0
        Transmission_AS5 = 0
        Transmission_AS6 = 0
        Transmission_AS7 = 0
        Transmission_AS8 = 0
        Transmission_AS9 = 0
        Transmission_AV = 0
        Transmission_AV10 = 0
        Transmission_AV6 = 0
        Transmission_AV7 = 0
        Transmission_AV8 = 0
        Transmission_M5 = 0
        Transmission_M6 = 0
        Transmission_M7 = 0

        Fuel_Type_D = request.form['Fuel Type_D']  # Assuming fuel_type is a string

        Fuel_Type_D = 1
        Fuel_Type_E = 0
        Fuel_Type_N = 0
        Fuel_Type_X = 0
        Fuel_Type_Z = 0
        
        Fuel_Consumption_City = float(request.form['Fuel Consumption City (L/100 km)'])
        Fuel_Consumption_Hwy = float(request.form['Fuel Consumption Hwy (L/100 km)'])
        Fuel_Consumption_Comb_KM = float(request.form['Fuel Consumption Comb (L/100 km)'])
        Fuel_Consumption_Comb_MPG = float(request.form['Fuel Consumption Comb (mpg)'])
   
        data = [Engine_Size, Cylinders, Transmission_A10, Transmission_A4, Transmission_A5, Transmission_A6, Transmission_A7, Transmission_A8, Transmission_A9, Transmission_AM5, Transmission_AM6, Transmission_AM7, Transmission_AM8, Transmission_AM9, Transmission_AS10, Transmission_AS4, Transmission_AS5, Transmission_AS6, Transmission_AS7, Transmission_AS8, Transmission_AS9, Transmission_AV, Transmission_AV10, Transmission_AV6, Transmission_AV7, Transmission_AV8, Transmission_M5, Transmission_M6, Transmission_M7, Fuel_Type_D, Fuel_Type_E, Fuel_Type_N, Fuel_Type_X, Fuel_Type_Z, Fuel_Consumption_City, Fuel_Consumption_Hwy, Fuel_Consumption_Comb_KM, Fuel_Consumption_Comb_MPG]

        print('checkpredictiondataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', data)
        data = np.array(data).reshape(1, -1)  # Reshape to correct dimensions
        print('printreshapedataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', data)
        
        # Assuming PredictionPipeline is correctly imported and initialized
        obj = PredictionPipeline()
        predict = obj.predict(data)

        return render_template('results.html', prediction=str(predict))
    
    except Exception as e:
        print('The Exception message is:', e)
        return 'Something went wrong'



if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080, debug=True)
	# app.run(host="0.0.0.0", port = 8080)