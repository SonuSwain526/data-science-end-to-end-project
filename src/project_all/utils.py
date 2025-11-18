import mysql.connector
from src.project_all.logger import logger
from src.project_all.exception import customExeption
import sys
import pandas as pd
import os

def connectSql():
    try:
        # Connect to server
        cnx = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="Gourab@123",
            database="student_Engmnt"
        )

        df = pd.read_sql_query("""SELECT * FROM sstudent_engagement_dataset;""", cnx)
        # df_path = os.path.join("src", "project_all")
        # df.to_csv("data.csv")

        # print(df.head())

        return df

    except Exception as e:
        logger.error("Database connection failed")
        raise customExeption(e, sys)

    finally:
        try:
            cnx.close()
        except:
            pass

# connectSql()