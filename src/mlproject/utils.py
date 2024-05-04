import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
passw = os.getenv("password")
db = os.getenv('db')


def read_sql_data():
    '''Reading Sql Data and converting into Dataframe.'''
    
    logging.info("Reading SQL database starts")    
    try:
        mydb = pymysql.connect(
            host=host, 
            user=user, 
            password=passw, 
            db=db
        )
        logging.info(f"connection established {mydb}")
        df = pd.read_sql_query('Select * from student', mydb)
        print(df.head())
        
        
        return df
        
        
    except Exception as e:
        raise CustomException(e,sys)