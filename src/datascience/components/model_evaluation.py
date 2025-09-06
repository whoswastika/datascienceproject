import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib

from src.datascience.entity.config_entity import ModelEvaluationConfig
# from src.datascience.utils.common import save_json
from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories,save_json

class ModelEvaluation:
    def __init__(self,config : ModelEvaluationConfig):
        self.config = config
        
    def eval_metrics(Self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.drop(self.config.target_column, axis=1)
        test_y = test_data[self.config.target_column]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)
            
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            scores = {"rsme": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)
            mlflow.log_params(self.config.all_params)
            
            # print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (self.config.all_params.alpha, self.config.all_params.l1_ratio))
            # print("  RMSE: %s" % rmse)
            # print("  MAE: %s" % mae)
            # print("  R2: %s" % r2)
            
            # mlflow.log_param("alpha", self.config.all_params.alpha)
            # mlflow.log_param("l1_ratio", self.config.all_params.l1_ratio)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)
            
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model")