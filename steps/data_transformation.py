import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from utils.logger import logging
from utils.exception import CustomException
import sys
import joblib

'''
This module provides set of functions that will be use to clean & transform the data


'''


def cleaning_train_pipeline(df):

    
    try:

        logging.info("Start Transforming Data....")
    

        logging.info("-> Droping ID column")
        # 1. drop id column
        df.drop(columns = 'Applicant_ID', inplace=True)
        
        logging.info("-> Droping duplicate")
        # 2. drop duplicate column
        df.drop_duplicates(inplace=True)
        
        
        # 3. get the cat and num col
        cat_columns = [column for column in df.columns if df[column].dtype == 'object']
        num_columns = [column for column in df.columns if df[column].dtype != 'object']
        

        logging.info("-> Splitting to X and y")
        # 4. split the file into train and test
        X = df.drop(columns = 'Loan_Default_Risk').copy()
        y = df['Loan_Default_Risk'].copy()
        
        X_train, X_test, y_train, y_test = train_test_split(X,y, 
                                    random_state=42,  
                                    test_size=0.1,
                                        shuffle=True)
        
        
        logging.info("-> Applying Ordinal Encoder")
        
        # 5. apply encoder to the cat variable
        encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
        encoder.fit(X_train[cat_columns])

        X_train[cat_columns] = encoder.transform(X_train[cat_columns])    
        X_test[cat_columns] = encoder.transform(X_test[cat_columns])


        logging.info("-> Applying Standard Scaler")
        
        # 6. apply standardization to all X feature
        scaler = StandardScaler()

        scaler.fit(X_train)

        X_train= scaler.transform(X_train)
        X_test= scaler.transform(X_test)

        
        logging.info("-> Saving encoder and standardization file")

        #utils.save_object('artifacts',encoder)
        joblib.dump(encoder, 'encoder.pkl')
        joblib.dump(scaler, 'scaler.pkl')


        #utils.save_object('artifacts',scaler)

        return X_train, y_train, X_test, y_test

    except Exception as e:
        raise CustomException(e, sys)



# ---------------

# Maliciounes
# # Droping id column
# def drop_id_column(df: pd.DataFrame, column_name:str) -> pd.DataFrame:
#     return df.drop(columns = column_name)


# # Dropping duplicates
# def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:

#     first_size = df.shape[1]
#     df.drop_duplicates(inplace=True)
#     last_size = df.shape[1] - first_size

#     print(f'Drop {last_size} Duplicates')
#     return df





