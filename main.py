import streamlit as st
import joblib
import mlflow
from production import firebase as fb

#from mlflow import MlflowClient


# Credential Path
cred_path = 'production/cred/firebase_connector.json'
collection_name = 'loan_application_input'

@st.cache_resource
def get_ml_models(uri):

    mlflow.set_tracking_uri(uri)
    client = mlflow.MlflowClient()

    # get the staging model from experiment
    for model in client.search_registered_models(filter_string="name LIKE '%'"):
        for model_version in model.latest_versions:
            if model_version.current_stage == 'Staging':
                deployment_model = model_version
                # get the model
                model_path = f'runs:/{deployment_model.run_id}/loan_application_model'
                loaded_model = mlflow.pyfunc.load_model(model_path)

                print(f"name={model_version.name}; run_id={model_version.run_id}; version={model_version.version}, stage={model_version.current_stage}")

    return loaded_model


@st.cache_resource
def get_preprocessing(file_name):
    path = 'experiment/'
    preprocessing_file = joblib.load(path + file_name)

    return preprocessing_file


@st.cache_resource
def get_firebase(cred_path, collection_name):
    db = fb.connect_firestore(cred_path, collection_name)
    return db



def upload_firebase(db, collection_name, data):

    doc_ref = db.collection(collection_name).document()
    doc_ref.set(data)

    #return doc_ref
    


# import preprocessing model and train model

ml_model_url = 'https://dagshub.com/Syamil-Ali/Loan_Application_ML.mlflow'
ml_model = get_ml_models(ml_model_url)


# #utils.save_object('artifacts',encoder)
encoder = get_preprocessing('encoder.pkl')
scaler = get_preprocessing('scaler.pkl')

# # load model
# model_path = f'runs:/{deployment_model.run_id}/loan_application_model'

# loaded_model = mlflow.pyfunc.load_model(model_path)



# get db
db = get_firebase(cred_path, collection_name)
#doc_ref = fb.connect_firestore(cred_path, collection_name)


# -----------------------------
# start designing the streamlit ui

# ------------ part here from st_ppss

import streamlit as st
import pandas as pd

df = pd.read_csv('data/Applicant-details.csv')

st.title('Loan Application Classification',)
st.write('')


# ------------- cleanup function
# trying to predict
def cleanup(df):

    cat_columns = [column for column in df.columns if df[column].dtype == 'object']
    df[cat_columns] = encoder.transform(df[cat_columns])
    df = scaler.transform(df)

    return df

# ---------------- add form

with st.form("my_form"):

    st.markdown("**Personal Info**")

    # Applicant Age
    age = st.number_input('Age', min_value=18, max_value=100)

    #Residence_City	
    city = st.selectbox('City Reside',
                        df['Residence_City'].drop_duplicates())
    

    #Residence_state
    state = st.selectbox('State Reside',
                        df['Residence_State'].drop_duplicates())

    # marital status
    marital_st = st.radio('Marital Status', 
                        ['Single', 'Married'],
                        horizontal = True)

    #House_Ownership	
    house_owner = st.radio('House Ownership',
                            ['Rented', 'Owned', 'norent_noown'], horizontal=True)



    # Vehicle Ownership
    vehicle_owner = st.radio('Own Vehicle',
                            ['Yes', 'No'], horizontal=True)


    # years current residence
    years_residence = st.number_input('Total years in current residence', min_value=0, max_value=100)


    st.write('---')

    st.markdown("**Job Info**")

    # Occupation
    occupation = st.selectbox('Occupation',
                        df['Occupation'].drop_duplicates())

    # annual income
    annual_income = st.number_input('Annual Income ($)', min_value=0)

    # work experince
    experience = st.number_input('Total years working experience', min_value=0, max_value=100)


        
    # years current employment
    years_employment = st.number_input('Total in years current employment', min_value=0, max_value=100)


    st.write('---')
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")


if submitted:

    # combine all the result
    user_input = {
        'Annual_Income': annual_income,	
        'Applicant_Age': age,
        'Work_Experience': experience,
        'Marital_Status': marital_st,
        'House_Ownership': house_owner,
        'Vehicle_Ownership(car)' : vehicle_owner,
        'Occupation': occupation,
        'Residence_City': city,
        'Residence_State': state,
        'Years_in_Current_Employment': years_employment,	
        'Years_in_Current_Residence': years_residence	
    }

    # update to 
    
    user_input_df = pd.DataFrame(user_input, index=[0])

    model_input = cleanup(user_input_df)


    # prediction
    result = ml_model.predict(model_input)

    # update the db
    user_input['Loan_Application_Pred'] = int(result[0])


    #upload_firebase(db, collection_name, user_input)
    #doc_ref.set(user_input)
    
    print(user_input)


    #st.dataframe(user_input_df)
    prediction_convert = ":green[Approved]" if result[0] == 1 else ":red[Not Approved]"
    st.write('')
    st.write('')

    st.markdown(f"Loan Prediction: **{prediction_convert}**")
    #st.write(result[0])




















