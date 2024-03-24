import sys
from .logger import logging


"""
This module provides functions for custom exception handling

Functions:
    error_message_detail: read the error and provide the customize them

"""


# create custom error message
def error_message_detail(error, error_detail:sys): #expect it to be sys object type

    _,_, exc_tb = error_detail.exc_info() # get execution info
    
    file_name =  exc_tb.tb_frame.f_code.co_filename # get the error file name

    error_message = "Error occured in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message



class CustomException(Exception):

    def __init__(self, error, error_detail:sys):
        
        super().__init__(error) # get access to the error_detail class object 
        
        self.error_message = error_message_detail(error, error_detail= error_detail)

        logging.critical(self.error_message)
    # basically on why need to access the object for the error_message is because
    # --> raise CustomException(e, sys) ... (just look back at the raise exception)
    # --> e is the Exception type of object, so need to get access to the object


    def __str__(self):
        return self.error_message