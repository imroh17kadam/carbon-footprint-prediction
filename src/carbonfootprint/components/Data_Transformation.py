import os
from carbonfootprint import logger
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from carbonfootprint.entity.config_entity import DataTransformationConfig
from sklearn.preprocessing import StandardScaler
import pickle

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up

    def catrgorical_encoding(self):
        self.df = pd.read_csv(self.config.data_path)

        cat_features = ['Transmission', 'Fuel Type']
        self.df_new = self.df

        # Apply One-Hot Encoding using str.get_dummies() for each categorical feature
        for feature in cat_features:
            dummies = self.df[feature].str.get_dummies()
            self.df_new = pd.concat([self.df_new, dummies.add_prefix(feature + '_')], axis=1)

        columns_to_drop = ['Make', 'Model', 'Vehicle Class', 'Transmission', 'Fuel Type']
        self.df_new = self.df_new.drop(columns=columns_to_drop)

        new_column_order = [
            'Engine Size(L)', 'Cylinders',
            'Transmission_A10', 'Transmission_A4', 'Transmission_A5', 'Transmission_A6', 'Transmission_A7', 
            'Transmission_A8', 'Transmission_A9', 'Transmission_AM5', 'Transmission_AM6', 'Transmission_AM7', 
            'Transmission_AM8', 'Transmission_AM9', 'Transmission_AS10', 'Transmission_AS4', 'Transmission_AS5', 
            'Transmission_AS6', 'Transmission_AS7', 'Transmission_AS8', 'Transmission_AS9', 'Transmission_AV', 
            'Transmission_AV10', 'Transmission_AV6', 'Transmission_AV7', 'Transmission_AV8', 'Transmission_M5', 
            'Transmission_M6', 'Transmission_M7', 'Fuel Type_D', 'Fuel Type_E', 'Fuel Type_N', 'Fuel Type_X', 
            'Fuel Type_Z', 'Fuel Consumption City (L/100 km)', 'Fuel Consumption Hwy (L/100 km)', 
            'Fuel Consumption Comb (L/100 km)', 'Fuel Consumption Comb (mpg)', 'CO2 Emissions(g/km)'
        ]

        # Reorder the columns in the DataFrame
        self.df_final = self.df_new[new_column_order]

        self.df_new.shape


    def train_test_spliting(self):

        # Split the data into training and test sets. (0.75, 0.25) split.
        # train, test = train_test_split(self.df_new)
        train, test = train_test_split(self.df_final)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)


    def standardization(self):

        sc = StandardScaler()

        train_data = pd.read_csv('artifacts\\data_transformation\\train.csv')
        test_data = pd.read_csv('artifacts\\data_transformation\\test.csv')


        input_feature_train_df = train_data.drop(columns=['CO2 Emissions(g/km)'], axis=1)
        target_feature_train_df = train_data['CO2 Emissions(g/km)']

        input_feature_test_df = test_data.drop(columns=['CO2 Emissions(g/km)'], axis=1)
        target_feature_test_df = test_data['CO2 Emissions(g/km)']
        
        input_feature_train_arr = sc.fit_transform(input_feature_train_df)
        input_feature_test_arr = sc.transform(input_feature_test_df)

        train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
        test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

        logger.info(f"Saved preprocessing object.")

        pickle.dump(sc, open('artifacts\data_transformation\scaling.pkl', 'wb'))

        print('Standardized Train Data', train_arr)
        print('Standardized Test Data', test_arr)

        return (train_arr, test_arr)