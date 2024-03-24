import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from utils.logger import logging
from mlflow.models import infer_signature



# define evaluation metrics
def evaluation_metrics(y_test, y_pred):

    report = classification_report(y_test, y_pred, output_dict=True)
    sample_classification = pd.DataFrame(report).transpose()

    return sample_classification


# For this exercise is logistic regression

def train_model(X_train, y_train, X_test, y_test, params:dict):

    logging.info("Running up Logistic Regression...")

    # run logistic regression model
    model = LogisticRegression(**params)
    model.fit(X_train, y_train)

    score_train = model.score(X_train, y_train)
    score_valid = model.score(X_test, y_test)


    # trying to get the signature 
    # -> (responsible to save the schema of model input and output)
    predictions = model.predict(X_test)
    signature = infer_signature(X_test, predictions)



    return model, score_train, score_valid, signature

    
