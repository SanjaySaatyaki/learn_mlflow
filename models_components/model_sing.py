import warnings
import argparse
import logging
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn
from pathlib import Path
import os
from mlflow.models.signature import ModelSignature, infer_signature
from mlflow.types.schema import Schema, ColSpec


logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

#get arguments from command
parser = argparse.ArgumentParser()
parser.add_argument("--alpha", type=float, required=False, default=0.5)
parser.add_argument("--l1_ratio", type=float, required=False, default=0.5)
args = parser.parse_args()

#evaluation function
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Read the wine-quality csv file from local
    data = pd.read_csv("tracking_components\\red-wine-quality.csv")
    # os.mkdir("data/")
    data.to_csv("data/red-wine-quality.csv", index=False)
    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)
    train.to_csv("data/train.csv")
    test.to_csv("data/test.csv")
    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    alpha = args.alpha
    l1_ratio = args.l1_ratio
    # mlflow.set_tracking_uri(uri='./tracks')
    # print(mlflow.get_tracking_uri())

    # exp_id = mlflow.create_experiment(name="experiment_uri_artifact",tags={"version":"v1","priority":"p1"},
    #                                   artifact_location=Path.cwd().joinpath("test_artifacts").as_uri())
    # exp = mlflow.get_experiment(exp_id)
    # print(exp)
    mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")
    exp = mlflow.set_experiment("experiment_auto_log")
    print(exp)

    with mlflow.start_run(experiment_id=exp.experiment_id,run_name="run_1"):
        lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        
        mlflow.sklearn.autolog(
            log_input_examples=False,
            log_model_signatures=False,
            log_models=False
        )
        
        lr.fit(train_x, train_y)
        
        
        predicted_qualities = lr.predict(test_x)

        (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

        print("Elasticnet model (alpha={:f}, l1_ratio={:f}):".format(alpha, l1_ratio))
        print("  RMSE: %s" % rmse)
        print("  MAE: %s" % mae)
        print("  R2: %s" % r2)

        signature = infer_signature(model_input=test_x,model_output=predicted_qualities)
        input_examples = {
            "columns":np.array(test_x.columns),
            "data":np.array(test_x.values)
        }

        mlflow.sklearn.log_model(lr,"model",signature=signature,input_example=input_examples)
        
        
    
    ls_run = mlflow.last_active_run()
    print(ls_run.info)