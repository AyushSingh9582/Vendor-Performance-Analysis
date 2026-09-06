import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s-%(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')

# Hardcoded path to your CSVs
DATA_DIR = r"C:\Users\Ayush\Downloads\data\data"

def ingest_db(df, table_name, engine):
    '''This function will ingest the dataframe into database table'''
    # FIX: Added chunksize=10000 to process the insertion in batches
    df.to_sql(table_name, con=engine, if_exists='replace', index=False, chunksize=10000)

def load_raw_data():
    '''This function will load the CSVs as DataFrame and ingest into db'''
    start = time.time()
    for file in os.listdir(DATA_DIR):
        if '.csv' in file:
            file_path = os.path.join(DATA_DIR, file)
            # Optional: If you still hit memory limits reading the file itself, 
            # you can also add chunksize here (e.g., pd.read_csv(file_path, chunksize=50000))
            df = pd.read_csv(file_path)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df, file[:-4], engine)
            
    end = time.time()
    total_time = (end - start)/60
    logging.info('----------------Ingestion Complete----------------')
    # Pro-tip: Added :.2f to round your minutes nicely in the logs!
    logging.info(f'\nTotal Time Taken: {total_time:.2f} minutes')

if __name__ == '__main__':
    load_raw_data()