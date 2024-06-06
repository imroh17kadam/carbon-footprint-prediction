import pandas as pd
import os
from carbonfootprint import logger
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import joblib
from carbonfootprint.entity.config_entity import ModelTrainerConfig
import pickle


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self, scaled_train_array, scaled_test_array):
        # X_train,X_test,y_train,y_test=(
        #     train_array[:,:-1],
        #     train_array[:,-1],
        #     test_array[:,:-1],
        #     test_array[:,-1]
        # )

        X_train = scaled_train_array[:, :-1]
        y_train = scaled_train_array[:, -1]
        X_test = scaled_test_array[:, :-1]
        y_test = scaled_test_array[:, -1]

        #  Linear Regression
        # lr = LinearRegression()
        # lr.fit(X_train, y_train)

        rf = RandomForestRegressor(n_estimators = self.config.n_estimators, min_samples_split = self.config.min_samples_split, max_features = self.config.max_features, max_depth = self.config.max_depth, criterion = self.config.criterion)
        rf.fit(X_train, y_train)

        y_train_pred = rf.predict(X_train)
        y_test_pred = rf.predict(X_test)

        scaler = pickle.load(open('c:\\Users\\Admin\\Desktop\\Rohit\\MachineLearning\\ml-mlops-workflow\\artifacts\\data_transformation\\scaling.pkl', 'rb'))

        # print('Checksingletestdataaaaaa', X_test[1].reshape(1,-1))
        # single_pred = rf.predict(scaler.transform(X_test[1].reshape(1,-1)))
        # print('single prediction data', single_pred)

        print("training score = ",rf.score(X_train,y_train))
        print("testing score = ",rf.score(X_test,y_test))
        print(y_train_pred, y_test_pred)
        
        logger.info("Train and Test scores")
        logger.info(rf.score(X_train,y_train))
        logger.info(rf.score(X_test,y_test))

        joblib.dump(rf, os.path.join(self.config.root_dir, self.config.model_name))

        return(y_test, y_test_pred, y_train, y_train_pred)