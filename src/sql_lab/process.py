import logging
import os
import mysql.connector
import pandas as pd

#read the database info from the environemnt variables
DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBNAME = os.getenv("DBNAME")

def read_data(filename):
    """read csv file and return as dataframe"""
    logging.info("Reading data")
    df = pd.read_csv(filename)
    return df

def clean_data(data):
    """return dataframe without rows with missing values"""
    logging.info("Cleaning data")
    data = data.dropna()
    return data

def load_data(data, table):
    """create mock table and load into mysql"""
    logging.info("Loading data")
    try:
        #connect to database
        db = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME
        )
        cursor = db.cursor()

        #create mock table
        query = """
        CREATE TABLE IF NOT EXISTS mock (
            id BIGINT,
            `group` VARCHAR(255),
            name VARCHAR(255),
            gender VARCHAR(255),
            color VARCHAR(255),
            city VARCHAR(255)
        )
        """
        cursor.execute(query)

        #insert each row using query
        query = (
            "INSERT INTO mock "
            "(id, `group`, name, gender, color, city) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )

        for row in data.itertuples(index=False, name=None):
            cursor.execute(query, row)

        #commit changes
        db.commit()
        logging.info("Data loaded successfully")
        cursor.close()
        db.close()

    except mysql.connector.Error as e:
        logging.error("Error: %s", e)

def main():
    """run read_data, clean_data, and load_data"""
    data = read_data("MOCK_DATA.csv")
    data = clean_data(data)
    load_data(data, "mock")

if __name__ == "__main__":
    main()
