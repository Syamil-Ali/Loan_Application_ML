import streamlit as st
#import joblib
#import mlflow
#from mlflow import MlflowClient


# mlflow.set_tracking_uri('https://dagshub.com/Syamil-Ali/Loan_Application_ML.mlflow')
# client = mlflow.MlflowClient()

# for model in client.search_registered_models(filter_string="name LIKE '%'"):
#     for model_version in model.latest_versions:
#         if model_version.current_stage == 'Staging':
#             deployment_model = model_version
#         print(f"name={model_version.name}; run_id={model_version.run_id}; version={model_version.version}, stage={model_version.current_stage}")


# # import preprocessing model and train model

# #utils.save_object('artifacts',encoder)
# encoder = joblib.load('./experiment/encoder.pkl')
# scaler = joblib.load('./experiment/scaler.pkl')

# # load model
# model_path = f'runs:/{deployment_model.run_id}/loan_application_model'

# loaded_model = mlflow.pyfunc.load_model(model_path)


# -----------------------------
# start designing the streamlit ui
st.title("Loan Application Classification")