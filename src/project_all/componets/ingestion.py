from src.project_all.logger import logger
from src.project_all.exception import customExeption
from sklearn.model_selection import train_test_split
from src.project_all.utils import connectSql
import sys

import os
from dataclasses import dataclass

@dataclass
class pathInitalize():
    RAW_DATA_PATH : str = os.path.join("artifacts", "data.csv")
    TRAIN_DATA_PATH : str = os.path.join("artifacts", "train.csv")
    TEST_DATA_PATH : str = os.path.join("artifacts", "test.csv")

class dataIngestion:
    def __init__(self):
        self.data_paths = pathInitalize

    def ingetion(self):
        try:
            logger.info("splitting data...")
            df = connectSql()
            os.makedirs(os.path.dirname(self.data_paths.RAW_DATA_PATH), exist_ok=True)
            df.to_csv(self.data_paths.RAW_DATA_PATH, index=False)
            #train test split
            train_data, test_data = train_test_split(df,test_size=0.2, random_state=42)
            train_data.to_csv(self.data_paths.TRAIN_DATA_PATH, index = False)
            test_data.to_csv(self.data_paths.TEST_DATA_PATH, index = False)
            logger.info("splitted the data.")
            return (train_data, test_data)


        except Exception as e:
            logger.error("something in splitting.")
            raise customExeption(e, sys)

# ob = pathInitalize()
# ob1 = dataIngestion()
# ob1.ingetion()