import logging
import os
from datetime import datetime


"""
Utility functions for logging.

This module provides functions for configuring logging settings and defining custom exceptions.

Functions:
    setup_logging: Configure logging settings.
    CustomException: Custom exception class for handling errors.

"""


#** i changed the code here a bit, if got error, please revised the code back

# Logging file path configuration
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # define file name using date format
logs_path = os.path.join(os.getcwd(),"logs", LOG_FILE) # define the targeted path to store the file

# Create the path, if it exist then skip
os.makedirs(logs_path, exist_ok=True) # create the logging file


LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) # define the targeted path


logging.basicConfig(
    filename = LOG_FILE_PATH,
    format =  "[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO, # has many (can check documentation), but .INFO is just level for general information
)