"""datasource.py

Should get queries from the water data
"""

import psycopg2 as ps
import psqlConfig as config

def connect():
    """Establishes a connection to the database with the following credentials:
        user - username, which is also the name of the database
        password - the password for this database on perlman

    Returns: a database connection.

    Note: exits if a connection cannot be established.
    """
    try:
        connection = ps.connect(database=config.database, user=config.user, password=config.password, host="localhost")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection

def get_year_and_location_sql(connection, year:int, location) -> list:
    """ This def function should ask for an input of the year and location from the user and return all of the information about that year and location

    Args:
        connection (psycopg2.connection) - the connection to the database
        year (int) - the specified year
        location (text) - the specified location

    Returns:
        list - a list of all the information when the year is the same, and the country is the same, or None if the query fails.
    """
    try:
        cursor = connection.cursor()
        """when the location is a country"""
        query = f"SELECT * FROM water_country WHERE country=%s AND year_n=%s;"
        """when the location is a region"""
        query = f"SELECT * FROM water_region WHERE region=%s AND year_n=%s;"
        cursor.execute(query, (location, year,))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def get_only_location_sql(connection, location) -> list:
    """This def function should ask for an input of the location from the user and return all of the information about that location

    Args:
        connection (psycopg2.connection) - the connection to the database
        location (text) - the specified location

    Returns:
        list - a list of all the information when the location is the same, or None if the query fails.
    """
    try:
        cursor = connection.cursor()
        """when the location is a country"""
        query = f"SELECT * FROM water_country WHERE country=%s;"
        """when the location is a region"""
        query = f"SELECT * FROM water_region WHERE region=%s;"
        cursor.execute(query, (location,))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def main():
    # Connect to the database
    connection = connect()

    # Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
    year_and_location = get_year_and_location_sql(connection, 2000, "Australia and New Zealand")
    
    location = get_only_location_sql(connection, "Australia and New Zealand")

    
    if year_and_location is not None:
        print("Query results: ")
        for item in year_and_location:
            print(item)

    if location is not None:
        print("Query results: ")
        for item in location:
            print(item)

    # Disconnect from database
    connection.close()

main()