import joblib 
import numpy as np
import pandas as pd
from pathlib import Path



class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    

    
    def predict(self, data):
        prediction = self.model.predict(data)

        # Code for restrict number to 2 decimal places
        # number = np.array([prediction])  # Example as a single element array
        # rounded_number = np.round(number, 2)

        return prediction