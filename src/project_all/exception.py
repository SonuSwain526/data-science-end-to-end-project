from src.project_all.logger import logger
import sys

def get_Detail_err(error_msg, detailerr):
    """
    For extracting detailed information about the error:
    - File name
    - Line number
    - Actual error message
    """
    _, _, exc_tb = detailerr.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename  # File where the error occurred
    line_number = exc_tb.tb_lineno                  # Line number of the error

    # Formatted error message
    error_message = (
        f"Error occurred in python script [{file_name}] "
        f"at line [{line_number}]: {str(error_msg)}"
    )

    return error_message

class customExeption(Exception):
    def __init__(self, error_msg, detailerr : sys):
        super().__init__(error_msg)
        self.error_msg = get_Detail_err(error_msg, detailerr)

    def __str__(self):
        return self.error_msg