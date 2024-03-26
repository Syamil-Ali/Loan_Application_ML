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

# ------------ part here from st_ppss

import streamlit as st
import pandas as pd

df = pd.read_csv('Exercise Loan Application/data/Applicant-details.csv')

st.title('Loan Application Classification')


# ---------------- add form

# Applicant_ID	(none)
# Annual_Income	
# Applicant_Age	
# Work_Experience	
# Marital_Status	
# House_Ownership	
# Vehicle_Ownership(car)	
# Occupation	
# Residence_City	
# Residence_State	
# Years_in_Current_Employment	
# Years_in_Current_Residence	
# Loan_Default_Risk

with st.form("my_form"):

    st.write("Inside the form")


    # annual income
    an_income = st.number_input('Annual Income ($)', min_value=0)

    # Applicant Age
    age = st.number_input('Age', min_value=18, max_value=100)

    # work experince
    experience = st.number_input('Total years working experience', min_value=0, max_value=100)

    # marital status
    marital_st = st.radio('Marital Status', 
                        ['Single', 'Married'],
                        horizontal = True)
    
    #House_Ownership	
    house_owner = st.radio('House Ownership',
                            ['Rented', 'Owned', 'norent_noown'])


    # Vehicle Ownership
    vehicle_owner = st.radio('Own Vehicle',
                            ['Yes', 'No'])


    # Occupation
    occupation = st.selectbox('Occupation',
                        df['Occupation'].drop_duplicates())

    #Residence_City	
    city = st.selectbox('City Reside',
                        df['Residence_City'].drop_duplicates())
    

    #Residence_state
    city = st.selectbox('State Reside',
                        df['Residence_State'].drop_duplicates())


        
    # years current employment
    years_employment = st.number_input('Total in current employment', min_value=0, max_value=100)


    # years current residence
    years_employment = st.number_input('Total in current residence', min_value=0, max_value=100)

    
    



    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")


if submitted:
    st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

