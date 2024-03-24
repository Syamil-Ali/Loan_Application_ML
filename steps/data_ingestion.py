import pandas as pd
import numpy as np
from utils.logger import logging
import sys
from utils.exception import CustomException

"""
This module provides functions for reading data file

Functions:
    data_ingest: Ingest data from a specified file path.

"""

def data_ingest(data_path: str) -> pd.DataFrame:
    
    logging.info("Ingesting Data")
    try:
        df = pd.read_csv(data_path)
        return df

    except Exception as e:
        raise CustomException(e,sys) from None