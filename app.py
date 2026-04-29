from flask import Flask
import csv
from ProductionCode.command_line import *

loadData()

app = Flask(__name__)
PORT = 5100

county_data = []
region_data = []

@app.route('/')
def homepage():
    '''the initial homepage'''
    return "hello, this is the homepage"

@app.route('/<string:location>/<string:year>')
def get_year_and_location_route(location: str, year: str) -> str:
    '''app route when a user inputs a spcific location and year to return the string of the information there'''
    getting_year_and_location = getData(location.strip(), year.strip())
    print(getting_year_and_location)
    return str(getting_year_and_location)

@app.route('/search/l/<string:location>')
def get_location_information(location: str) -> str:
    '''app route when a user only inputs a specific location and it'll return all the information about the country throughout the years'''
    getting_location_information = getData(location.strip(), None)
    print(getting_location_information)
    return str(getting_location_information)

@app.errorhandler(404)
def page_not_found(e):
     '''For route error'''
     return "sorry, wrong format, do this instead...."

@app.errorhandler(500)
def python_bug(e):
     '''For python error'''
     return "Something went wrong in our Python code"

if __name__ == '__main__':
    app.run(port=PORT)