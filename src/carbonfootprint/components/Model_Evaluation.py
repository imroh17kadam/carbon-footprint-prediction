import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from carbonfootprint.entity.config_entity import ModelEvaluationConfig
from carbonfootprint.constants import *
from carbonfootprint.utils.common import save_json



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self, y_test, y_test_pred, y_train, y_train_pred):
        print('predicted actual', y_test)
        print('predicted pred', y_test_pred)

        # pred_df = pd.DataFrame({'Actual Value':actual,'Predicted Value':pred,'Difference':actual-pred})
        # print('predicted and actual', pred_df)

        train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
        train_mae = mean_absolute_error(y_train, y_train_pred)
        train_r2 = r2_score(y_train, y_train_pred)

        rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
        mae = mean_absolute_error(y_test, y_test_pred)
        r2 = r2_score(y_test, y_test_pred)

        print('train_rmse = ', train_rmse, 'train_mae = ', train_mae, 'train_r2 = ', train_r2)
        print('test_rmse = ', rmse, 'test_mae = ', mae, 'test_r2 = ', r2)

        return rmse, mae, r2
    


    def log_into_mlflow(self, y_test, y_test_pred, y_train, y_train_pred):

        model = joblib.load(self.config.model_path)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():


            (rmse, mae, r2) = self.eval_metrics(y_test, y_test_pred, y_train, y_train_pred)
            
            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)


            # Model registry does not work with file store
            if tracking_url_type_store != "file":

            #     # Register the model
            #     # There are other ways to use the Model Registry, which depends on the use case,
            #     # please refer to the doc for more information:
            #     # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="RandomForestModel")
            else:
                mlflow.sklearn.log_model(model, "model")