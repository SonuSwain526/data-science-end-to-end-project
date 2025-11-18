from src.project_all.logger import logger
from src.project_all.exception import customExeption
from src.project_all.componets.ingestion import dataIngestion


import sys

if __name__ == "__main__":
    logger.info("execution started")
    try:
        # intiligeIngetion = dataIngestion()
        train_data, test_data = dataIngestion().ingetion()
        # x = 2/0
    except Exception as e:
        logger.info("error in exception")
        raise customExeption(e, sys)