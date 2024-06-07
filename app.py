from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from carbonfootprint.pipeline.prediction import PredictionPipeline
import pickle



app = Flask(__name__) # initializing a flask app
scaler = pickle.load(open('./artifacts/data_transformation/scaling.pkl', 'rb'))


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
        Transmission_AM9 = 0
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

        Fuel_Type_D = 0
        Fuel_Type_E = 0
        Fuel_Type_N = 0
        Fuel_Type_X = 0
        Fuel_Type_Z = 0

        # Read the inputs given by the user
        Engine_Size = float(request.form['Engine Size(L)'])
        Cylinders = int(request.form['Cylinders'])
        
        transmission_type = request.form['Transmission_A10']  

        if transmission_type == 'A10':
            Transmission_A10 = 1
        elif transmission_type == 'A4':
            Transmission_A4 = 1
        elif transmission_type == 'A5':
            Transmission_A5 = 1
        elif transmission_type == 'A6':
            Transmission_A6 = 1
        elif transmission_type == 'A7':
            Transmission_A7 = 1
        elif transmission_type == 'A8':
            Transmission_A8 = 1
        elif transmission_type == 'A9':
            Transmission_A9 = 1
        elif transmission_type == 'AM5':
            Transmission_AM5 = 1
        elif transmission_type == 'AM6':
            Transmission_AM6 = 1
        elif transmission_type == 'AM7':
            Transmission_AM7 = 1
        elif transmission_type == 'AM8':
            Transmission_AM8 = 1
        elif transmission_type == 'AM9':
            Transmission_AM9 = 1
        elif transmission_type == 'AS10':
            Transmission_AS10 = 1
        elif transmission_type == 'AS4':
            Transmission_AS4 = 1
        elif transmission_type == 'AS5':
            Transmission_AS5 = 1
        elif transmission_type == 'AS6':
            Transmission_AS6 = 1
        elif transmission_type == 'AS7':
            Transmission_AS7 = 1
        elif transmission_type == 'AS8':
            Transmission_AS8 = 1
        elif transmission_type == 'AS9':
            Transmission_AS9 = 1
        elif transmission_type == 'AV':
            Transmission_AV = 1
        elif transmission_type == 'AV10':
            Transmission_AV10 = 1
        elif transmission_type == 'AV6':
            Transmission_AV6 = 1
        elif transmission_type == 'AV7':
            Transmission_AV7 = 1
        elif transmission_type == 'AV8':
            Transmission_AV8 = 1
        elif transmission_type == 'M5':
            Transmission_M5 = 1
        elif transmission_type == 'M6':
            Transmission_M6 = 1
        elif transmission_type == 'M7':
            Transmission_M7 = 1

        Fuel_Type = request.form['Fuel Type_D']  

        if Fuel_Type == 'D':
            Fuel_Type_D = 1
        elif Fuel_Type == 'E':
            Fuel_Type_E = 1
        elif Fuel_Type == 'N':
            Fuel_Type_N = 1
        elif Fuel_Type == 'X':
            Fuel_Type_X = 1
        elif Fuel_Type == 'Z':
            Fuel_Type_Z = 1
        
        Fuel_Consumption_City = float(request.form['Fuel Consumption City (L/100 km)'])
        Fuel_Consumption_Hwy = float(request.form['Fuel Consumption Hwy (L/100 km)'])
        Fuel_Consumption_Comb_KM = float(request.form['Fuel Consumption Comb (L/100 km)'])
        Fuel_Consumption_Comb_MPG = float(request.form['Fuel Consumption Comb (mpg)'])
   
        data = [Engine_Size, Cylinders, Transmission_A10, Transmission_A4, Transmission_A5, Transmission_A6, Transmission_A7, Transmission_A8, Transmission_A9, Transmission_AM5, Transmission_AM6, Transmission_AM7, Transmission_AM8, Transmission_AM9, Transmission_AS10, Transmission_AS4, Transmission_AS5, Transmission_AS6, Transmission_AS7, Transmission_AS8, Transmission_AS9, Transmission_AV, Transmission_AV10, Transmission_AV6, Transmission_AV7, Transmission_AV8, Transmission_M5, Transmission_M6, Transmission_M7, Fuel_Type_D, Fuel_Type_E, Fuel_Type_N, Fuel_Type_X, Fuel_Type_Z, Fuel_Consumption_City, Fuel_Consumption_Hwy, Fuel_Consumption_Comb_KM, Fuel_Consumption_Comb_MPG]

        print('Check Data List', np.array(data).reshape(1, -1))
        data = np.array(data).reshape(1, -1)  # Reshape to correct dimensions
        new_data = scaler.transform(list(data))
        print('Check reshaped data', new_data)
        
        obj = PredictionPipeline()
        predict = obj.predict(new_data)

        return render_template('results.html', prediction=str(predict))
    
    except Exception as e:
        print('The Exception message is:', e)
        return 'Something went wrong'



if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)