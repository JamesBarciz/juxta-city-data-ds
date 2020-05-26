from flask import Flask, jsonify, request, json, render_template
from flask_cors import CORS
import pandas as pd

# This dataframe contains heart disease data and COVID-19
# data by county (by city is too difficult as there are cities,
# towns and boroughs and data like that is not available.
# Dataframe column[0] is an unnamed column that resulted from
# putting the dataframe into a CSV with no specified index.

unique_city_health_stats = pd.read_csv('./unique_cities_health_stats.csv').drop(columns='Unnamed: 0')
# print(unique_city_health_stats.shape)
# print(unique_city_health_stats.head())

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('homepage.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/team")
def team():
    return render_template('team.html')
