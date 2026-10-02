import logging
import os
import mysql.connector

DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBNAME = os.getenv("DBNAME")


def get_data_by_group(value):
    """return rows from mock table where the group is same as value argument"""
    logging.info("get data by group")

    try:
        #connect to the database
        db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME)
        cursor = db.cursor(dictionary=True)

        #select rows that match the griup value
        query = "SELECT * FROM mock WHERE `group` = %s"
        cursor.execute(query, (value,))
        results = cursor.fetchall()
        cursor.close()
        db.close()
        return results
    except mysql.connector.Error as e:
        logging.error("Error: %s", e)

def plot_counts(groupby):
    """count the number fo rows with distinct values in the column."""
    logging.info("getting count of rows in the column wiht distinct values")

    try:
        #connect to database
        db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME)
        cursor = db.cursor()

        #count rows for each value
        query = "SELECT `group`, COUNT(*) FROM mock GROUP BY `group`"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        db.close()
        return results
    except mysql.connector.Error as e:
        logging.error("Error: %s", e)

def main():
    """run and display the database queries"""
    group_data = get_data_by_group("provide a list of 3-5 items")
    print(group_data)
    counts = plot_counts("group")
    print(counts)

if __name__ == "__main__":
    main()
