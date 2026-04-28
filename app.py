from flask import Flask
import csv
from ProductionCode.command_line import *

app = Flask(__name__)

county_data = []

region_data = []

# def load_data():
#     '''Loads data from weather.csv into data global variable'''
#     if len(county_data) == 0:
#         with open('ProductionCode/Water_country.csv', newline='') as f:
#             reader = csv.reader(f)
#             for row in reader:
#                 county_data.append(row)

#     if len(region_data) == 0:
#         with open('ProductionCode/Water_region.csv', newline='') as f:
#             reader = csv.reader(f)
#             for row in reader:
#                 region_data.append(row)

@app.route('/')
def homepage():
    return "hello, this is the homepage"

# app route when a user inputs a spcific location and year to return
# the string of the information there
@app.route('/<string:location>/<string:year>')
def get_year_and_location_route(location: str, year: str) -> str:
    getting_year_and_location = getData(location.strip(), year.strip())
    return str(getting_year_and_location)

# app route when a user only inputs a specific location and it'll return
# all the information about the country throughout the years
@app.route('/search/l/<string:location>')
def get_location_information(location: str) -> str:
    getting_location_information = getData(location.strip(), None)
    return str(getting_location_information)

@app.errorhandler(404)
def page_not_found(e):
     return "sorry, wrong format, do this instead...."

@app.errorhandler(500)
def python_bug(e):
     return "Something went wrong in our Python code"

if __name__ == '__main__':
    # load_data()
    app.run(port=5100)