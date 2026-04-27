from flask import Flask
import csv
from command_line.py import *

app = Flask(__name__)

data = []

def load_data():
    '''Loads data from weather.csv into data global variable'''
    if len(data) == 0:
        with open('Water_country.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)

@app.route('/')
def homepage():
    return "hello, this is the homepage"

@app.route('/<int:row>/<int:col>/')
def get_cell(row: int, col: int) -> str:
    return str(data[row][col])

@app.route('/r/<int:row>/')
def get_row(row: int) -> str:
    return str(data[row])

@app.errorhandler(404)
def page_not_found(e):
     return "sorry, wrong format, do this instead...."

@app.errorhandler(500)
def python_bug(e):
     return "Something went wrong in our Python code"



if __name__ == '__main__':
    load_data()
    app.run(port=5100)